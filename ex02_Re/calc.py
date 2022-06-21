import tkinter as tk
import tkinter.messagebox as tkm
# if__name__=="__main__":
def button_click(event):
    button=event.widget
    i=button["text"]
    tkm.showinfo=("",f"{i}のボタンがクリックされました")
root=tk.Tk()
root.title("練習問題")
root.geometry("300x500")

x,y=0,0
for i in range(9,-1,-1):
    button=tk.Button(root,text=f"{i}",width=4,height=2
                 ,font=("Times New Roman",30)
                 )
    button.grid(row=x,column=y)
    y+=1
    if (i)%3==0:
        x+=1
        y=0
    button.bind("<1>",button_click)
root.mainloop()