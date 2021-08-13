import random
import sys, os, time


"""
共通鍵暗号方式.
メッセージを暗号化する鍵と復号する鍵が同じ方式.
シーザー暗号, AES, DESが代表的.
ここではシーザー暗号で実装.

sender:メッセージの送り手
receiver:メッセージの受け手
msg:通信路にあるメッセージ
key:通信路にある鍵

senderが持つメッセージmsgと, 通信路にあるメッセージmsgが同じ値だと内容が漏洩している事になる.
senderはmsgをkeyを使って暗号化してから送った為, 
通信路にあるmsgは, keyを使って復号出来ないと内容が読み取れない.

ただし, keyを手に入れてしまえば復号出来, 第三者であっても内容が分かってしまう.
その為, keyをどのように共有するかという鍵配送問題を解決しないと, 暗号化の意味がなくなる.
"""

class User:
    def gen_key(self):
        self.key = random.randint(1, 10)

    def receive_key(self, key):
        self.key = key

    def gen_msg(self):
        self.msg = "abc"

    def receive_msg(self, msg):
        dec_msg = decryption(msg, self.key)
        self.msg = dec_msg

    def send_msg(self):
        enc_msg = encryption(self.msg, self.key)
        return enc_msg

    def send_key(self):
        return self.key

    def get_msg(self):
        return self.msg

def encryption(msg, key):
    enc_msg = ""

    for m in msg:
        ord_num = None #基準となるアスキーコード
        if 'A' <= m <= 'Z':
            ord_num = ord('A')
            
        elif 'a' <= m <= 'z':
            ord_num = ord('a')

        if ord_num is not None:
            x = ord(m)
            n = ord_num + key
            enc_msg += chr(((x - n) % 26) + ord_num)
        else:
            enc_msg += m

    return enc_msg

def decryption(msg, key):
    dec_msg = ""

    for m in msg:
        ord_num = None #基準となるアスキーコード
        if 'A' <= m <= 'Z': 
            ord_num = ord('A')
            
        elif 'a' <= m <= 'z': 
            ord_num = ord('a')

        if ord_num is not None:
            x = ord(m)
            n = ord_num - key
            dec_msg += chr(((x - n) % 26) + ord_num) #文字xをn個のシフトをして,基準となるアスキーコード分の数を加える
        else:
            dec_msg += m

    return dec_msg



def main1():
    #ユーザーの生成
    sender = User()
    receiver = User()

    #送信するメッセージと鍵を送り手が生成
    sender.gen_key()
    sender.gen_msg()

    #送り手がメッセージを送信
    key = sender.send_key()
    msg = sender.send_msg()
    
    
    #受け手がメッセージを受信
    receiver.receive_key(key)
    receiver.receive_msg(msg)
    

    #メッセージが正しく受け取れたか, 漏洩していないかを確認
    print("sender msg :", sender.get_msg())
    print("communication channel :", msg)
    print("receiver msg :", receiver.get_msg())

def main2():
    #ユーザーの生成
    sender = User()
    receiver = User()

    #送信するメッセージと鍵を送り手が生成
    sender.gen_key()
    sender.gen_msg()

    #送り手がメッセージを送信
    key = sender.send_key()
    msg = sender.send_msg()
    
    
    #受け手がメッセージを受信
    receiver.receive_key(key)
    receiver.receive_msg(msg)
    

    #通信路にあるkeyを使って第三者がmsgを復号する事で漏洩
    print("sender msg :", sender.get_msg())
    print("communication channel :", decryption(msg, key))
    print("receiver msg :", receiver.get_msg())

if __name__ == "__main__":
    #通信が漏洩していない場合
    print("通信が漏洩していない場合")
    main1()

    #通信が漏洩している場合
    print("\n通信が漏洩している場合")
    main2()

    


    