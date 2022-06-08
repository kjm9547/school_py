import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfile
from turtle import window_width

def open_f():
    file = askopenfilename(title=".파일선택",filetypes=(("텍스트 파일","*,txt"),("all files", "*.*")))
    window.title(os.path.basename(file)+ " - 메모장")
    text.delete(1.0,END)
    f=open(file, "r")
    text.insert(1.0,f.read())
    f.close()
def save_f():
    file = filedialog.asksaveasfile(parent=window, mode="w")
    if file != None:
        lines = text.get('1.0',END + '-1c')
        file.write(lines)
        file.close()

def exit_f():
    if messagebox.askokcancel("Quit", "종료하시겠습니까?"):
        window.destroy()
def new_f():
    text.delete(1.0,END)

def cut_e():
    global content
    content =text.get(SEL_FIRST,SEL_LAST)
    text.delete(SEL_FIRST,SEL_LAST)
def copy_e():
    global content
    content =text.get(SEL_FIRST,SEL_LAST)
def paste_e():
    global content
    text.insert(INSERT,content)
def delete_e():
    text.delete(SEL_FIRST,SEL_LAST)
window = Tk()
text = Text(window,width=50,height=30)
text.pack()

menu = Menu(window)
f_list = Menu(menu)
e_list = Menu(menu)
h_list = Menu(menu)

f_list.add_command(label="new",command=new_f)
f_list.add_command(label="open",command=open_f)
f_list.add_command(label="save",command=save_f)
f_list.add_command(label="exit",command =exit)
menu.add_cascade(label="File",menu=f_list)

e_list.add_command(label="cut",command=cut_e)
e_list.add_command(label="copy",command=copy_e)
e_list.add_command(label="paste",command=paste_e)
e_list.add_command(label="delete",command=delete_e)
menu.add_cascade(label="Edit",menu=e_list)

h_list.add_command(label="help")
menu.add_cascade(label="Help",menu=h_list)

window.config(menu=menu)
window.mainloop()