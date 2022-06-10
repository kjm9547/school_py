from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageDraw,ImageTk
from PIL import ImageFilter
from PIL.ImageFilter import BLUR
from tkinter.colorchooser import askcolor

mode = None
mycolor = "black"
mypenwidth = 5
oldx,oldy =None,None
tk =None
im =None
def initial():
    global tk,im
    im = Image.new("RGB",(840,640),color=(256,256,256))
    tk=ImageTk.PhotoImage(im)
    canvas.config(width=im.width,height=im.height)
    canvas.create_image(im.width/2,im.height/2,image=tk)
    window.update()
def reset(event):
    global oldx,oldy
    oldy,oldx = None,None
def paint(event):
    global im ,tk ,oldx,oldy
    fill_color = "white" if mode == "erase" else mycolor
    if oldx and oldy:
        canvas.create_line(oldx,oldy,event.x,event.y,fill=fill_color,width=mypenwidth)
        draw = ImageDraw.Draw(im)
        draw.line((oldx,oldy,event.x,event.y),fill=fill_color,width=mypenwidth)
    oldx = event.x
    oldy =event.y
        
def open_f():
    global im,tk
    fname = filedialog.askopenfilename()
    im = Image.open(fname)
    tk= ImageTk.PhotoImage(im)
    canvas.config(width=im.width,height=im.height)
    canvas.create_image(im.width/2,im.height/2,image=tk)
    window.update()

def saveimage():
    global im,fname
    fname = filedialog.asksaveasfilename(title="파일 저장",defaultextension="*.png",filetypes=(("png file","*.png")))
    im.save(fname)

def quit():
    window.quit()
def image_rotate():
    global im,tk
    im = im.rotate(45)
    tk = ImageTk.PhotoImage(im)
    canvas.create_image(250,250,image =tk)
    window.update()    
def image_blur():
    global im,tk
    im = im.filter(ImageFilter.BLUR)
def change_white_black():
    pass
def change_two_num():
    pass
def image_sharp():
    pass
def embosing():
    pass
def choose_color():
    global mycolor
    mycolor = askcolor(color=mycolor)[1]

window = Tk()
canvas = Canvas(window,width=600,height=600)
canvas.pack()
canvas.bind("<B1-Motion>",paint)
canvas.bind("<ButtonRelease-1>",reset)
menu = Menu(window)
f_list = Menu(menu)
m_list = Menu(menu)
w_list = Menu(menu)
initial()
menu.add_cascade(label="파일",menu=f_list)
f_list.add_command(label="열기",command=open_f)
f_list.add_command(label="저장",command=saveimage)
f_list.add_command(label="종료",command=quit)
menu.add_cascade(label="영상편집",menu=m_list)
m_list.add_command(label="영상회전",command=image_rotate)
m_list.add_command(label="영상흐리게",command=image_blur)
m_list.add_command(label="흑백영상",command=change_white_black)
m_list.add_command(label="이진화",command=change_two_num)
m_list.add_command(label="영상뚜렷하게",command=image_sharp)
m_list.add_command(label="엠보스",command=embosing)
menu.add_cascade(label="선조정",menu=w_list)
w_list.add_command(label="Line Color", command=choose_color)
w_list.add_separator()
window.config(menu=menu)

window.mainloop()