import random
import datetime
a=random.dandint(0,2)
X=["サザエの旦那の名前は?"]
Y=["カツオの妹の名前は?"]
Z=["タラオはカツオから見てどんな関係?"]
XX=["マスオ","ナミヘイ"]
YY=["ワカメ","コンブ"]
ZZ=["甥","おいっこ"]
S=[X,Y,Z]
SS=[XX,YY,ZZ]
def shutudai (a):
    r=random.choice(S)
    print(r)
    return
    
def kaito(seikai):
    ans=input("解答を入力してください")
    if ans in seikai:
        print("正解です")
    else:
        print("不正解です")


