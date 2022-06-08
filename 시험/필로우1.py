from tkinter import *
from tkinter import Canvas, Menu, Tk, Widget, filedialog as fd

from PIL import ImageTk,Image

def open():
    global im, tk_img
    fname  = fd.askopenfilename()
    im = Image.open(fname)
    tk_img = ImageTk.PhotoImage(im)
    canvas.config(width=im.width,height=im.height)
    canvas.create_image(im.width/2,im.height/2,imgae=tk_img)
    window.update()

window=Tk()
canvas = Canvas(window,width=500,height=500)
canvas.pack()
menu = Menu(window)
f_list = Menu(menu)
m_list = Menu(menu)
w_list = Menu(menu)

menu.add_cascade(label="파일",menu=f_list)
f_list.add_command(label="열기",command=open)
#f_list.add_command(label="저장",command=saveimage)
#f_list.add_command(label="종료",command=quit)
menu.add_cascade(label="영상편집",menu=m_list)
#m_list.add_command(label="영상회전",command=image_rotate)
#m_list.add_command(label="영상흐리게",command=image_blur)
#m_list.add_command(label="흑백영상",command=change_white_black)
#m_list.add_command(label="이진화",command=change_two_num)
#m_list.add_command(label="영상뚜렷하게",command=image_sharp)
#m_list.add_command(label="엠보스",command=embosing)
menu.add_cascade(label="선조정",menu=w_list)
#w_list.add_command(label="Line Color",command=choose_color)
#w_list.add_command(label="넓이 2",command=change_width_2)
#w_list.add_command(label="넓이 5",command=change_width_5)
#w_list.add_command(label="넓이 8",command=change_width_8)
window.config(menu=menu)
window.mainloop()