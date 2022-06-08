from glob import escape
import os
from re import T
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import FileDialog, askopenfilename


def new_file():
    text.delete(1.0,END)
    
def open_file():
    file = askopenfilename(title="파일선택",filetypes=(("턱스트 파일", "*.txt"),
    ("all files","*.*")))
    window.title(os.path.basename(file) + " - 메모장")
    text.delete(1.0,END)
    f=open(file,"r")# "R"은 읽기 모드를 뜻함 
    text.insert(1.0, f.read())#read() 파일을 읽어오는 메소드  파일전체를 하나의 문자열로 가져온다.
    f.close()    
    
def save_file():
    file = filedialog.asksaveasfile(parent=window, mode='w')
    if file != None:
        lines = text.get('1.0',END)
        file.write(lines)
        file.close()
def exit():
    if messagebox.askokcancel("Quit","종료하시겠습니까?"):
        window.destroy()

def cut():
    global g_t
    g_t= text.get(SEL_FIRST,SEL_LAST)
    text.delete(SEL_FIRST,SEL_LAST)
def copy():
    global g_t
    g_t= text.get(SEL_FIRST,SEL_LAST)
def paste():
    global g_t
    text.insert(1.0,g_t)
def delete():
    text.delete(1.0,END)
def about():
    label = messagebox.showinfo("About", "메모장 프로그램")

window  = Tk()
text = Text(window, width=100,height=40)

menu = Menu(window)
F_list = Menu(menu)
E_list = Menu(menu)
H_list = Menu(menu)
F_list.add_command(label="New",command=new_file)
F_list.add_command(label="Open",command=open_file)
F_list.add_command(label="Save",command= save_file)
F_list.add_command(label="Exit",command=exit)

E_list.add_command(label= "Cut",command=cut)
E_list.add_command(label= "Copy",command=copy)
E_list.add_command(label= "Paste",command=paste)
E_list.add_command(label= "Delete",command=delete)

H_list.add_command(label="NotePadInto",command=about)

menu.add_cascade(label = "File",menu = F_list)
menu.add_cascade(label = "Edit",menu = E_list)
menu.add_cascade(label = "Help",menu = H_list)

text.pack()
window.config(menu=menu)
window.mainloop()