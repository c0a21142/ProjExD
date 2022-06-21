import tkinter as tk
import tkinter.messagebox as tkm
def button_click(event):
    btn = event.widget
    num = btn['text']
    # tkm.showinfo(num, f"{num}のボタンがクリックされました")
    if num=="=":
        eqn=entry.get()
        res=eval(eqn)
        entry.delete(0,tk.END)
        entry.insert(tk.END,res)
    else:
        entry.insert(tk.END,num)


def click_CE(event):
    entry.delete("0","end")

def click_C(event):
    entry.delete("0","end")


def click_B(event):
    X= len(entry.get())-1
    entry.delete(X,tk.END)



root = tk.Tk()
root.title("練習問題")

# root.geometry("500x500")

entry=tk.Entry(root,width=30,justify="right",font=("Times New Roman", 20))
entry.insert(tk.END, "")
entry.grid(row=0,column=0, columnspan=5)


x,y = 1,1


for i, num in enumerate(["%","CE","C","B","1/x","**","**(1/2)","/","7","8","9","*","4","5","6","-","1","2","3","+","+/-","0",".","="],1):
    btn=tk.Button(root, text=num, font=("Times New Roman", 30),fg="#ffffff",bg="#000000")
    btn.bind("<1>", button_click)
    btn.grid(row=x, column=y)
    if  num=="CE":
        btn.bind("<1>", click_CE)
    elif num=="C":
        btn.bind("<1>", click_C)
    elif num=="B":
        btn.bind("<1>", click_B)

    if (i)%4==0:
        x+=1
        y=0
    y+=1
root.mainloop()
