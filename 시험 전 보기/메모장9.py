import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
def new_f():
    pass
def open_f():
    file = filedialog.askopenfilename(title="파일 선택",filetypes=("텍스트파일","*.txt"))
    window.title(os.path.basename(file)+"-메모장")
    text.delete(1.0,END)
    f=open(file)
    text.insert(1.0,f.read())
    f.close()
def save_f():
    file = filedialog.asksaveasfile(parent=window,mode="w")
    if text != None:
        lines = text.get(1.0,END)
        file.write(lines)
        file.close()
def exit():
    label =messagebox.showinfo("정보","하이요")
    if messagebox.askokcancel("","  "):
        window.destroy
    
        

def cut_e():
    pass
def copy_e():
    pass
def paste_e():
    pass
def delete_e():
    pass

window = Tk()
text = Text(window,width=50,height=40)
text.grid(sticky= N + E + S + W)

scrollbar = Scrollbar(text)
text = Text(window,yscrollcommand=scrollbar.set)
text.pack(side="left",fill="both",expand=True)
scrollbar.pack(side=RIGHT,fill=Y)

menu = Menu(window)
list_f = Menu(menu)
e_list = Menu(menu)
h_list = Menu(menu)

menu.add_cascade(label="File",menu=list_f)
list_f.add_command(label="new",command=new_f)
list_f.add_command(label="save",command=open_f)
list_f.add_command(label="open",command=save_f)
list_f.add_command(label="exit",command =exit)

e_list.add_command(label="cut",command=cut_e)
e_list.add_command(label="copy",command=copy_e)
e_list.add_command(label="paste",command=paste_e)
e_list.add_command(label="delete",command=delete_e)
menu.add_cascade(label="Edit",menu=e_list)

h_list.add_command(label="help")
menu.add_cascade(label="Help",menu=h_list)

window.config(menu=menu)

window.mainloop()