from tkinter import Button, Entry, Tk
from tkinter.constants import END


list = ['7','8','9','/','C','4','5', '6', '*', ' ','1', '2', '3', '-', ' ','0', '.', '=', '+', ' ' ]

window = Tk()
entry = Entry(window)
entry.grid(row=0,column=0,columnspan=5)
r = 1
c = 0
def cal(self):
    resut = str(eval(entry.get())) 
    entry.insert(END,"="+resut)
def click(w):
    if w == "=":
        resut = str(eval(entry.get())) 
        entry.insert(END,"="+resut)
    elif w=="C":
        entry.delete(0,END)
    else:
        entry.insert(END,w)
for word in list:
    def process(w=word):
        click(w)
    Button(window,width=5,command=process,text=word).grid(row=r,column=c)
    c+=1
    if c==5:
        r+=1
        c=0
entry.bind("<Return>",cal)
window.mainloop()