from email.mime import image
from fnmatch import fnmatchcase
from textwrap import fill
import tkinter as tk
from tkinter.colorchooser import askcolor
from tkinter.tix import IMAGE
from PIL import Image, ImageTk, ImageFilter, ImageDraw
from tkinter import Canvas, filedialog as fd

window = tk.Tk()
canvas = tk.Canvas(window, bg="white", height=840, width=680)
im,img,mode,mycolor,lastx,lasty,mypenwidth=None,None,None,None,None,None,5

def open():
    global im, img
    fname = fd.askopenfilename()
    im = Image.open(fname)
    img = ImageTk.PhotoImage(im)
    canvas.config(width=im.width, height=im.height)
    canvas.create_image(im.width/2, im.height/2,image=img)
    window.update()

def quit():
    window.quit()

def image_rotate():
    global img, im
    im = im.rotate(45)
    img = ImageTk.PhotoImage(im)
    canvas.create_image(250, 250, image=img)
    window.update()

def image_blur():
    global img, im
    im = im.filter(ImageFilter.BLUR)
    img = ImageTk.PhotoImage(im)
    canvas.create_image(250, 250, image=img)
    window.update()

def image_black():
    global img, im
    im = im.convert('L')
    img = ImageTk.PhotoImage(im)
    canvas.create_image(250, 250, image=img)
    window.update()

def image_two():
    global img, im
    im = im.convert('1')
    img = ImageTk.PhotoImage(im)
    canvas.create_image(250, 250, image=img)
    window.update()

def image_e():
    global img, im
    im = im.filter(ImageFilter.EMBOSS)
    img = ImageTk.PhotoImage(im)
    canvas.create_image(250, 250, image=img)
    window.update()

def image_s():
    global img, im
    im = im.filter(ImageFilter.SHARPEN)
    img = ImageTk.PhotoImage(im)
    canvas.create_image(250, 250, image=img)
    window.update()

def save_image():
    global im,fname
    fname = fd.asksaveasfilename(title="파일 선택", defaultextension=".png",filetypes=(("png file", "*.png"),
    ("jpg file", "*.jpg"), ("gif file", "*.gif"), ("all files", "*.*")))
    im.save(fname)

def change_width():
    global mypenwidth
    mypenwidth = 2

def change_width2():
    global mypenwidth
    mypenwidth = 5

def change_width3():
    global mypenwidth
    mypenwidth = 8

def reset(event):
    global lastx, lasty
    lastx, lasty = None, None

def paint(event):
    global lastx, lasty, mode, mycolor
    fill_color = 'white' if mode == "erase" else mycolor
    if lastx and lasty:
        canvas.create_line(lastx, lasty, event.x, event.y, width=mypenwidth, fill=fill_color)
        draw = ImageDraw.Draw(im)
        draw.line((lastx, lasty, event.x, event.y), width=mypenwidth, fill=fill_color)
    lastx = event.x
    lasty = event.y

def choose_color():
    global mycolor
    mycolor = askcolor(color=mycolor)[1]

def in_image():
    global im, img
    im = Image.new('RGB', (840, 680), color=(256,256,256))
    img = ImageTk.PhotoImage(im)
    canvas.config(width=im.width, height=im.height)
    canvas.create_image(im.width/2, im.height/2,image=img)
    window.update()

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar)
ipmenu = tk.Menu(menubar)
wmenu = tk.Menu(menubar)
filemenu.add_command(label="열기", command=open)
filemenu.add_command(label="저장", command=save_image)
filemenu.add_separator()
filemenu.add_command(label="종료", command=quit)
ipmenu.add_command(label="영상회전", command=image_rotate)
ipmenu.add_command(label="영상흐리게", command=image_blur)
ipmenu.add_command(label="흑백영상", command=image_black)
ipmenu.add_command(label="이진화", command=image_two)
ipmenu.add_command(label="영상뚜렷하게", command=image_s)
ipmenu.add_command(label="엠보스", command=image_e)
wmenu.add_command(label="Line Color", command=choose_color)
wmenu.add_separator()
wmenu.add_command(label="넓이 2", command=change_width)
wmenu.add_command(label="넓이 5", command=change_width2)
wmenu.add_command(label="넓이 8", command=change_width3)
menubar.add_cascade(label="파일", menu=filemenu)
menubar.add_cascade(label="영상처리", menu=ipmenu)
menubar.add_cascade(label="선색 두께", menu=wmenu)


canvas.bind("<B1-Motion>", paint)
canvas.bind('<ButtonRelease-1>', reset)
canvas.pack()
in_image()
window.config(menu=menubar)
window.mainloop()

    
