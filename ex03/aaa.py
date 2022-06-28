import tkinter as tk
from turtle import bgcolor
import maze_maker as mm
import tkinter.messagebox as tkm

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ''

def main_proc():
    global cx, cy, key, mx, my

    delta={
        "Up":[0,-1],
        "Down":[0,+1],
        "Left":[-1,0],
        "Right":[+1,0],
    }
  
    if key == "Up" and maze_bg[my-1][mx]==0:
        my-=1
    if key == "Down" and maze_bg[my+1][mx]==0:
        my+=1
    if key == "Left" and maze_bg[my][mx-1]==0:
        mx-=1
    if key == "Right" and maze_bg[my][mx+1]==0:
        mx+=1
    cx = mx*100+50
    cy = my*100+50
    if cx==1350 and cy==750:
        tkm.showinfo("タイトル", "ゴール！")

    canvas.create_rectangle(cx-50, cy-50, cx+50, cy+50, 
                                     fill="green",tag="bg")

    canvas.lift("tori", "bg")

    canvas.coords("tori",cx,cy)
    root.after(100, main_proc)

    

if __name__=="__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root, width=1500,height=900, bg="black")
    canvas.pack()

    maze_bg = mm.make_maze(15,9)
    mm.show_maze(canvas, maze_bg)
    mx=1
    my=1

    tori = tk.PhotoImage(file="fig/8.png")
    tori2 = tk.PhotoImage(file="fig/8.png")

    cx, cy=300, 400

    
    canvas.create_image(cx,cy, image=tori, tag="tori")
    
    canvas.create_image(1350, 750, image=tori2, tag="tori2")

    key=""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    root.after(100, main_proc)

    root.mainloop()