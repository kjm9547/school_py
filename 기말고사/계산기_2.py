from ast import Return
from tkinter import *
def cal(self):
    result = eval(entry.get())
    s = str(result)
    entry.insert(END, "="+s)

def click(key):
    if key == "=":
        result =eval(entry.get())
        s = str(result)
        entry.insert(END,"="+s)
    elif key=='C':
        entry.delete(0,END)
    else:
        entry.insert(END,key)
bt_list = ['7','8','9','/','C',
'4','5', '6', '*', ' ',
'1', '2', '3', '-', ' ',
'0', '.', '=', '+', ' ' ]
window = Tk()
entry=Entry(window,width=30)
entry.grid(row=0,column=0,columnspan=5)
entry.bind("<Return>",cal)

row_i = 1
col_i = 0
for bt_text in bt_list:
    def process(t=bt_text):
        click(t)
    Button(window,text=bt_text,width=5,command=process).grid(row=row_i,column=col_i)
    col_i +=1
    if col_i == 5:
        col_i = 0
        row_i+=1
window.mainloop()