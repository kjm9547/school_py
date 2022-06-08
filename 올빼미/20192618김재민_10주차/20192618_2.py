from tkinter import*
window = Tk()
label = Label(window,text="hi")
label.grid(row=0,column=0,columnspan=3)

total=0
def update_add():
    update("add")
def update_minus():
    update("minus")
def update_reset():
    update("reset")
def update(method):
    global total
    if method == "add":
        total +=int(entry.get())
        label['text'] =str(total)
    elif method == "minus":
        total -=int(entry.get())
        label['text'] =str(total)    
    elif method == "reset":
        total = 0
        label["text"]= str(total)
        entry.delete(0,END)






entry = Entry(window,fg="black")
entry.grid(row=1,column=0,columnspan=3)
plus_bt = Button(window,text="더하기(+)",command=update_add)
plus_bt.grid(row=2,column=0)
minus_bt = Button(window,text="빼기(-)",command=update_minus)
minus_bt.grid(row=2,column=1)
reset_bt = Button(window,text="초기화",command=update_reset)
reset_bt.grid(row=2,column=2)

window.mainloop()