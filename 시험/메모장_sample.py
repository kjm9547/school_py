from tkinter import *


window = Tk()
text = Text(window,width=50,height=40)
text.pack()

menu = Menu(window)
list_f = Menu(menu)

menu.add_cascade(label="File",menu=list_f)
list_f.add_command(label="new")
list_f.add_command(label="save")
list_f.add_command(label="open")
list_f.add_command(label="exit")

window.config(menu=menu)

window.mainloop()