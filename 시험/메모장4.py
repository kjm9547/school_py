from decimal import MIN_ETINY
import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

def open_f():
    file = askopenfilename(title="파일선택",filetypes=(("파일선택","*.txt"),("all file","*.*")))
    window.title(os.path.basename(file+"- 메모장"))
    text.delete(1.0,END)
    f = open(file,"r")
    text.insert(1.0,f.read())
    f.close()
def save_f():
    file = filedialog.asksaveasfile(parent=window,mode="w")
    if text != None:
        lines = text.get('1.0',END)
        file.write(lines)
        file.close()
def exit_f():
    if messagebox.askokcancel("quit","종료하시겠습니까?"):
        window.destroy()
def new_f():
    text.delete(1.0,END)
window = Tk()
text = Text(window,width=50,height=40)

menu = Menu(window)
f_list = Menu(menu)

f_list.add_command(label="new",command=new_f)
f_list.add_command(label="open",command=open_f)
f_list.add_command(label="save",command=save_f)
f_list.add_command(label="exit",command=exit_f)

menu.add_cascade(label="file",menu=f_list)
text.pack()
window.config(menu=menu)
window.mainloop()