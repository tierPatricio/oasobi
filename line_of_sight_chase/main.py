##基本追跡とLOS追跡のシミュレーションをタイルベースの環境で行う
##10*10の座標上をPredator(追跡者)とPlayer(逃避者)が動き回る形
##Playerは一方向に等速度で動き,Predatorはそれを追跡,追いついた時終了
##Predatorを赤, Playerを青として, 3次元の画像をpltで表示させる

import numpy as np
import matplotlib.pyplot as plt

import sys, os, time

#const
HEIGHT, WIDTH = 10, 10
PLAYER_POS = (HEIGHT-1, 0)
PLAYER_VALUE = 1
PLAYER_COLOR = [0, 0, 255]
PLAYER_LOCAS_COLOR = [0, 0, 64]
PREDATOR_POS =  (0, 0)
PREDATOR_VALUE = 2
PREDATOR_COLOR = [255, 0, 0]
PREDATOR_LOCAS_COLOR = [64, 0, 0]


class Field:
    def __init__(self) -> None:
        self.field = np.zeros((HEIGHT, WIDTH), dtype=np.int8)
        self.locus = np.zeros((HEIGHT, WIDTH), dtype=np.int8) #移動の軌跡

    def remove_position(self, pos):
        self.field[pos] = 0

    def set_position(self, pos, val):
        self.field[pos] = val
        self.locus[pos] = val #ログに残す

    def move_position(self, cls):
        if cls.prev_pos != (None, None):
            self.remove_position(cls.prev_pos)
        self.set_position(cls.curr_pos, cls.val)

    def update(self, *unit_cls):
        for cls in unit_cls:
            self.move_position(cls)

    def show(self):
        print(self.field)

    def show_cv_init(self):
        self.fig, self.ax = plt.subplots(1, 2)
        image_field = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint16)
        log_field = np.copy(image_field)
        self.lines_image = self.ax[0].imshow(image_field)
        self.lines_log = self.ax[1].imshow(log_field)


    def show_cv(self):
        image_field = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint16)
        image_colors = {PLAYER_VALUE: PLAYER_COLOR, PREDATOR_VALUE: PREDATOR_COLOR}
        
        for key, val in image_colors.items():
            mask_field = self.field == key
            image_field[mask_field] = val


        log_field = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint16)
        image_colors = {PLAYER_VALUE: PLAYER_LOCAS_COLOR, PREDATOR_VALUE: PREDATOR_LOCAS_COLOR}
        for key, val in image_colors.items():
            mask_field = self.locus == key
            log_field[mask_field] = val
        

        self.lines_image.set_data(image_field)
        self.lines_log.set_data(log_field)

        plt.pause(.05)

    def isGameover(self):
        f_unq = np.unique(self.field)
        if PLAYER_VALUE not in f_unq:
            return True
        return False
    

class Unit:
    def __init__(self, name, pos, val) -> None:
        self.name = name
        self.prev_pos = (None, None)
        self.curr_pos = pos
        self.val = val

    def update_pos(self, next_pos):
        curr_pos = self.curr_pos
        self.prev_pos = curr_pos
        self.curr_pos = next_pos
    
#基本追跡する追跡者
def calc_predator_pos(predator_pos, target_pos):
    target_posY, target_posX = target_pos
    predator_posY, predator_posX = predator_pos

    if predator_posX > target_posX:
        predator_posX -= 1
    elif predator_posX < target_posX:
        predator_posX += 1

    if predator_posY > target_posY:
        predator_posY -= 1
    elif predator_posY < target_posY:
        predator_posY += 1

    return (predator_posY, predator_posX)

def calc_predator_pos_LOS(predator_pos, target_pos):
    #col = Y, row = X
    col, row = predator_pos
    end_col, end_row = target_pos
    next_col, next_row = predator_pos
    delta_col, delta_row = end_col - col, end_row - row

    #もしターゲットが動いていない場合pathRow, pathColは書き換えずにcurrent_stepを一個進めて計算量を減らす

    path_row, path_col = [-1 for i in range(HEIGHT*WIDTH)], [-1 for i in range(HEIGHT*WIDTH)]
    current_step = 0

    ##進行方向の計算
    if delta_col < 0: #Y軸で見て、ターゲットが追跡者より左にいる時左方向に進む(-1)
        step_col = -1
    else:
        step_col = 1

    if delta_row < 0: #X軸で見て、ターゲットが追跡者より上にいる時上方向に進む(-1)
        step_row = -1
    else:
        step_row = 1

    ##ブレゼンハムアルゴリズム
    if delta_col > delta_row:
        # fraction = delta_row * 2 - delta_col
        fraction = delta_row - delta_col / 2
        while (next_col != end_col):
            if fraction >= 0:
                next_row = next_row + step_row 
                fraction = fraction - delta_col
            next_col = next_col + step_col
            fraction = fraction + delta_row
            path_row[current_step] = next_row
            path_col[current_step] = next_col
            current_step += 1
    else:
        # fraction = delta_col * 2 - delta_row
        fraction = delta_col - delta_row / 2
        while (next_row != end_row):
            if fraction >= 0:
                next_col = next_col + step_col
                fraction = fraction - delta_row
            next_row = next_row + step_row
            fraction = fraction + delta_col
            path_row[current_step] = next_row
            path_col[current_step] = next_col
            current_step += 1

    # print("predator_pos: {}".format(predator_pos))
    # print("target_pos: {}".format(target_pos))
    # for i in range(len(path_col)):
    #     if path_col[i] < 0 or path_row[i] < 0:
    #         break
    #     print("*{}: {}, {}".format(i, path_col[i], path_row[i]))

    return (path_col[0], path_row[0])

#横一直線に移動する逃避者
def calc_player_pos(player_pos):
    player_posY, player_posX = player_pos
    if player_posX < WIDTH-1:
        player_posX += 1
    
    return (player_posY, player_posX)

def test():
    print("test\n")
    field = Field()
    player = Unit("player", PLAYER_POS, PLAYER_VALUE)
    predator = Unit("predator", PREDATOR_POS, PREDATOR_VALUE)
    field.update(player, predator)

    print(calc_predator_pos_LOS(predator.curr_pos, player.curr_pos))

def main_los():
    field = Field()
    player = Unit("player", PLAYER_POS, PLAYER_VALUE)
    predator = Unit("predator", PREDATOR_POS, PREDATOR_VALUE)
    field.update(player, predator)
    field.show_cv_init()
    field.show_cv()

    touch_flag = False
    
    while touch_flag is False:
        ##movement predator
        predator.update_pos(calc_predator_pos_LOS(predator.curr_pos, player.curr_pos))
        field.update(predator)
        field.show_cv()
        touch_flag = field.isGameover()
        
        ##movement player
        player.update_pos(calc_player_pos(player.curr_pos))
        field.update(player)
        field.show_cv()

    plt.show()

def main():
    field = Field()
    player = Unit("player", PLAYER_POS, PLAYER_VALUE)
    predator = Unit("predator", PREDATOR_POS, PREDATOR_VALUE)
    field.update(player, predator)
    field.show_cv_init()
    field.show_cv()

    touch_flag = False
    
    while touch_flag is False:
        ##movement predator
        predator.update_pos(calc_predator_pos(predator.curr_pos, player.curr_pos))
        field.update(predator)
        field.show_cv()
        touch_flag = field.isGameover()
        
        ##movement player
        player.update_pos(calc_player_pos(player.curr_pos))
        field.update(player)
        field.show_cv()

    plt.show()



if __name__ == "__main__":
    # main()
    main_los()
    # test()
