import random
import datetime
X=["サザエの旦那の名前は?"]
Y=["カツオの妹の名前は?"]
Z=["タラオはカツオから見てどんな関係?"]
S=[X,Y,Z]
def main():
    seikai=shutudai()
    kaito=(seikai)
def shutudai ():
    r=random.choice(S)
    print(r)
    return r
    
def kaito(seikai):
    ans=input("解答を入力してください")
    if ans in seikai:
        print("正解です")
    else:
        print("不正解です")


