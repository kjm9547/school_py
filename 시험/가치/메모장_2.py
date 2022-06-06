import os
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename, asksaveasfilename
from turtle import width
def openfile():
    file = askopenfilename(title="파일선택", filetypes=(("텍스트 파일", "*.txt"), 
    ("all files", "*.*")))
    window.title(os.path.basename(file) + " - 메모장")
    text.delete(1.0,END)
    f= open(file,"r")
    text.insert(1.0,f.read())
    f.close()
def save():
    file = filedialog.asksaveasfile(parent=window,mode='w')
    if file != None:
        lines = text
window = Tk()
text = Text(window,width=80,height=40)
text.pack()

menu = Menu(window)
f_list = Menu(menu)
e_list = Menu(menu)
h_list = Menu(menu)
menu.add_cascade(label="File",menu=f_list)
f_list.add_command(label="open",command=openfile)
f_list.add_command(label="save")
f_list.add_command(label="exit")
f_list.add_command(label="new")

menu.add_cascade(label="Edit",menu=e_list)
e_list.add_command(label="cut")
e_list.add_command(label="delete")
e_list.add_command(label="copy")
e_list.add_command(label="paste")

menu.add_cascade(label="Help",menu=h_list)
h_list.add_command(label="infor")

window.config(menu=menu)
window.mainloop()