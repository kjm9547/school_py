from tkinter import *

window = Tk()
window.title("app")
display = Entry(window, width=33, bg="yellow")
display.grid(row=0,column=0,columnspan=5)

def click(key):
    if key == "=":
        result = eval(display.get())#현재의 엔트리를 받아옴
        s = str(result)
        display.insert(END,"="+s)
    elif key == "C":
        display.delete(0,END)
    else:
        display.insert(END,key)

button_list = ['7','8','9','/','C','4','5', '6', '*', ' ','1', '2', '3', '-', ' ','0', '.', '=', '+', ' ' ]
row_index = 1
col_index = 0
for button_text in button_list:
    def process(t=button_text):
        click(t)
    Button(window,text=button_text,width=5,command=process).grid(row=row_index,column=col_index)
    col_index+=1
    if col_index>4:
        row_index+=1
        col_index=0
window.mainloop()