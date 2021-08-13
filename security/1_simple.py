import random
import sys, os, time


"""
人同士のやりとりを想定

sender:メッセージの送り手
receiver:メッセージの受け手
msg:通信路にあるメッセージ

senderが持つメッセージmsgと, 通信路にあるメッセージmsgが同じ値だと内容が丸見え
このコードだと通信内容は丸見え
"""

class User:
    def gen_msg(self):
        self.msg = random.randint(1, 10000)
    
    def send(self):
        return self.msg
    
    def receive(self, msg):
        self.msg = msg

    def get_msg(self):
        return self.msg 

if __name__ == "__main__":
    #ユーザーの生成
    sender = User()
    receiver = User()

    #送り手が送信するメッセージの生成
    sender.gen_msg()

    #送り手がメッセージを送信
    msg = sender.send()
    
    #受け手がメッセージを受信
    receiver.receive(msg)

    #メッセージが正しく受け取れたか, 漏洩していないかを確認
    print("communication channel :", msg)
    print("sender msg :", sender.get_msg())
    print("receiver msg :", receiver.get_msg())


    


    