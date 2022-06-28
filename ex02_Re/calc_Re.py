import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()
root.title("練習問題")

# root.geometry("300x450")

entry=tk.Entry(root,width=30,justify="right",font=("Times New Roman", 20))
entry.insert(tk.END, "")
entry.grid(row=0,column=0, columnspan=5)

r,c = 1,1

def button_click(event):
    btn = event.widget
    num = btn['text']
    # tkm.showinfo(num, f"{num}のボタンがクリックされました")
    entry.insert(tk.END, num)

def click_plus(event):
    entry.insert(tk.END,"+")
    
def click_equal(event):
    equal = entry.get()
    ans = eval(equal)
    entry.delete("0","end")
    print(ans)
    entry.insert(tk.END,str(ans))

def click_CE(event):
    entry.delete("0","end")

def click_del(event):
    pos_end_prev = len(entry.get())-1
    entry.delete(pos_end_prev,tk.END)

for i, num in enumerate(["%","CE","C","del","1/x","**","**(1/2)","/","7","8","9","*","4","5","6","-","1","2","3","+","+/-","0",".","="],1):

    btn=tk.Button(root, text=num, font=("Times New Roman", 30),fg="#ffffff",bg="#000000")

    btn.bind("<1>", button_click)
    if num=="=":
        btn.bind("<1>", click_equal)
    elif num=="+":
        btn.bind("<1>", click_plus)
    elif num=="CE":
        btn.bind("<1>", click_CE)
    elif num=="C":
        btn.bind("<1>", click_CE)
    elif num=="del":
        btn.bind("<1>", click_del)
        
    btn.grid(row=r, column=c, padx=10, pady=10)
    if i%4==0:
        r+=1
        c=0
    c+=1
# equal_btn.bind("<1>", click_equal)

root.mainloop()