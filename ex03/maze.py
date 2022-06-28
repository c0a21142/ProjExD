import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as mm
import wave
import winsound as ws
def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx,cy,key,mx,my
    # delta = {#キー：押されているキーkey/値：移動幅リスト[x,y]
    #     "Up"   :[0, -20],
    #     "Down" :[0, +20],
    #     "Left" :[-20, 0],
    #     "Right":[+20, 0],}
    # cx, cy = cx+delta[key][0], cy+delta[key][1]
    if key=="Up" and maze_bg[my-1][mx]==0:my-=1
    if key == "Down" and maze_bg[my+1][mx]==0:my+=1
    if key == "Left" and maze_bg[my][mx-1]==0:mx-=1
    if key == "Right" and maze_bg[my][mx+1]==0:mx+=1
    cx,cy=mx*100+50,my*100+50
    if cx==1350 and cy==750:
        tkm.showinfo("おめでとうございます","無限ループに陥りました")
    canvas.create_rectangle(cx-50, cy-50, cx+50, cy+50, fill="red",tag="bg")

    canvas.lift("tori", "bg")
    canvas.coords("tori",cx,cy)
    root.after(100,main_proc)

# def sound():
#     base=tk.Tk()
#     base2=tk.Tk()
#     sound_file="なんでしょう?.wav"
# channel=sounds.play(loop=sd_loop)

if __name__ == "__main__":
    
    root = tk.Tk()
    root.title("迷えるこうかとん")

    canvas = tk.Canvas(width=1500,height=900,bg="black")
    canvas.pack()
    maze_bg=mm.make_maze(15,9)
    mm.show_maze(canvas,maze_bg)
    mx=1
    my=1
    tori = tk.PhotoImage(file="fig/5.png")
    tori2 = tk.PhotoImage(file="fig/5.png")
    mx,my=1,1
    cx,cy = 300,400
    canvas.create_image(cx,cy,image=tori,tag="tori")
    canvas.create_image(1350, 750, image=tori2, tag="tori2")
    key = ""
    root.bind("<KeyPress>",key_down)

    root.bind("<KeyRelease>",key_up)

    main_proc()
    sound_name="sample.wav"
    ws.PlaySound(sound_name,ws.SND_ALIAS)
    root.mainloop()