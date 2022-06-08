from PIL import Image,ImageTk,ImageFilter,ImageDraw
import tkinter as tk
from tkinter import Canvas, filedialog as fd
from tkinter.colorchooser import askcolor
im =None
tk_img = None
mode = None
mycolor=None
old_x, old_y = None, None
mypenwidth = 5
def initialize_image():   
    global im, tk_img  
    im =  Image.new('RGB', (840, 680), color=(256,256,256))
    tk_img = ImageTk.PhotoImage(im)
    canvas.config(width=im.width, height=im.height)    
    canvas.create_image(im.width/2, im.height/2, image=tk_img)
    window.update()
def reset(event):   # 사용자가 마우스 버튼에서 손을 떼면 이전 점을 삭제한다.
    global old_x, old_y    
    old_x, old_y = None, None
def paint(event):   # 이전 점과 현재 점 사이를 직선으로 연결한다.
    global  im, mode, old_x, old_y
    fill_color = 'white' if mode == "erase" else mycolor
    if old_x and old_y:        # canvas에 그리기        
        canvas.create_line(old_x, old_y, event.x, event.y, width=mypenwidth, fill=fill_color)
        draw = ImageDraw.Draw(im)        
        draw.line((old_x, old_y, event.x, event.y), fill=fill_color, width = mypenwidth)
    old_x = event.x
    old_y = event.y


def choose_color(): # 색상 메뉴가 선택되면 사용자한테 색상을 요구한다.
    global mycolor    
    mycolor = askcolor(color=mycolor)[1]  
def change_width_2():
    global mypenwidth    
    mypenwidth =2
def change_width_5():
    global mypenwidth    
    mypenwidth = 5
def change_width_8():
    global mypenwidth    
    mypenwidth =8
def open():
    global im, tk_img
    fname = fd.askopenfilename()
    im = Image.open(fname)
    tk_img = ImageTk.PhotoImage(im)
    canvas.config(width=im.width,height=im.height)
    canvas.create_image(im.width/2,im.height/2,image=tk_img)
    window.update()

def saveimage():
    global im, fname
    fname = fd.asksaveasfilename(title="파일저장", defaultextension=".png",               
    filetypes=(("png file", "*.png"),  ("gif file", "*.gif"),                                 
    ("jpg file", "*.jpg"), ("all files", "*.*")))
    im.save(fname)
def quit():
    window.quit()

def image_rotate():    
    global im, tk_img    
    out = im.rotate(45)    
    tk_img = ImageTk.PhotoImage(out)    
    canvas.create_image(250, 250, image=tk_img)
    window.update()
def image_blur():    
    global im, tk_img    
    out = im.filter(ImageFilter.BLUR)    
    tk_img = ImageTk.PhotoImage(out)    
    canvas.create_image(250, 250, image=tk_img)    
    window.update()
def change_white_black():    
    global im, tk_img    
    out = im.convert("L")    
    tk_img = ImageTk.PhotoImage(out)    
    canvas.create_image(250, 250, image=tk_img)    
    window.update()
def change_two_num():
    global im, tk_img    
    out = im.convert("1")    
    tk_img = ImageTk.PhotoImage(out)    
    canvas.create_image(250, 250, image=tk_img)    
    window.update()
def embosing():
    global im, tk_img    
    out = im.filter(ImageFilter.EMBOSS)    
    tk_img = ImageTk.PhotoImage(out)    
    canvas.create_image(250, 250, image=tk_img)    
    window.update()
def image_sharp():
    global im, tk_img    
    out = im.filter(ImageFilter.SHARPEN)    
    tk_img = ImageTk.PhotoImage(out)    
    canvas.create_image(250, 250, image=tk_img)    
    window.update()

window = tk.Tk()
canvas = tk.Canvas(window,width=500,height=500)
canvas.bind("<B1-Motion>", paint)
canvas.bind('<ButtonRelease-1>', reset)
canvas.pack()
initialize_image()
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar)
filemenu_2 = tk.Menu(menubar)
filemenu_3=tk.Menu(menubar)
filemenu.add_command(label="열기",command=open)
filemenu.add_command(label="저장",command=saveimage)
filemenu.add_command(label="종료",command=quit)

menubar.add_cascade(label="파일", menu=filemenu)


filemenu_2.add_command(label="영상회전",command=image_rotate)
filemenu_2.add_command(label="영상흐리게",command=image_blur)
filemenu_2.add_command(label="흑백영상",command=change_white_black)
filemenu_2.add_command(label="이진화",command=change_two_num)
filemenu_2.add_command(label="영상뚜렷하게",command=image_sharp)
filemenu_2.add_command(label="엠보스",command=embosing)

menubar.add_cascade(label="영상처리",menu=filemenu_2)

filemenu_3.add_command(label="Line Color",command=choose_color)
filemenu_3.add_command(label="넓이 2",command=change_width_2)
filemenu_3.add_command(label="넓이 5",command=change_width_5)
filemenu_3.add_command(label="넓이 8",command=change_width_8)
menubar.add_cascade(label="선색 두께",menu=filemenu_3)

window.config(menu=menubar)


window.mainloop()
