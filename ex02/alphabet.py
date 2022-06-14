import random
# X=["A","B","C","D","E","F","G","H","I","j","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
X=[chr(c+65) for c in range(26)]
a=10 #大賞文字数
b=2 #欠損文字数

def main ():
    for i in range(5):
        X=kai=shutudai()
        if X==1:
            break

def shutudai():
    # [chr(c+65) for c in range(26)]：先生のコード(1行で)
    #全てのアルフェベットから10個をランダムに選択
    XA=random.sample((X),a)
    print(XA)
    #欠損文字を選択
    XB=[random.sample(XA),b]
    return XA

def kaito(kai):
    num=int(input("欠損文字はいくつあるでしょうか?"))
    if num==b:
        print("不正解です")
        return 0
    else:
        print("正解です,それでは具体的に欠損文字を１つずつ入力して下さい")
        for i in range(10):
            x=input(f"{i+1}つ目の文字を入力して下さい")
            if x!=kai:
                print("不正解です,またチャレンジして下さい")
            return 0
        print("正解です")

#未完成だよ！