import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.filedialog import askopenfile, askopenfilename

def open_f():
    file = askopenfilename(title="파일선택",filetypes=(("파일선택","*.txt"),("모든 파일","*.*")))
    window.title(os.path.basename(file)+" - 메모장")
    text.delete(1.0,END)
    f = open(file,"r")
    text.insert(1.0,f.read())
    f.close()
def save_f():
    file = filedialog.asksaveasfile(parent=window,mode="w")
    if text!=None:
        lines = text.get('1.0',END)
        file.write(lines)
        file.close()

def exit_f():
    if messagebox.askokcancel("quit","종료하시겠습니까?"):
        window.destroy()
def new_f():
    text.delete(1.0,END)


def copy_e():
    global es
    es = text.get(SEL_FIRST,SEL_LAST)
def cut_e():
    global es
    es = text.get(SEL_FIRST,SEL_LAST)
    text.delete(SEL_FIRST,SEL_LAST)
def paste_e():
    global es
    text.insert(INSERT,es)
def delete_e():
    text.delete(SEL_FIRST,SEL_LAST)
window = Tk()
text = Text(window,width=50,height=40)
text.pack()

menu = Menu(window)
list_f = Menu(menu)
e_list = Menu(menu)
menu.add_cascade(label="File",menu=list_f)
menu.add_cascade(label="File",menu=e_list)
list_f.add_command(label="new",command=new_f)
list_f.add_command(label="save",command=save_f)
list_f.add_command(label="open",command=open_f)
list_f.add_command(label="exit",command=exit_f)
e_list.add_command(label="cut",command=cut_e)
e_list.add_command(label="copy",command=copy_e)
e_list.add_command(label="paste",command=paste_e)
e_list.add_command(label="delete",command=delete_e)
menu.add_cascade(label="Edit",menu=e_list)

window.config(menu=menu)

window.mainloop()