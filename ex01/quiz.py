import random
import datetime
a=random.randint(0,2)
X=["サザエの旦那の名前は?"]
Y=["カツオの妹の名前は?"]
Z=["タラオはカツオから見てどんな関係?"]
XX=["マスオ","ナミヘイ"]
YY=["ワカメ","コンブ"]
ZZ=["甥","おいっこ"]
S=[X,Y,Z]
SS=[XX,YY,ZZ]
def shutudai (a):
    print(S[a])
    
    
def kaito(a):
    ans=input("解答を入力してください")
    if a==0 or a==1:
        if ans==SS[a][0] or ans==SS[a][1]:
            print("正解です")
        else:
            print("不正解です")
    else:
        if ans==SS[a][0] or ans==SS[a][1] or ans==SS[a][2] or ans==SS[a][3]:
            print("正解")
        else:
            print("不正解です")


