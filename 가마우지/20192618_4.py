from tkinter import*
window = Tk()
def do_convert():
    inch_val = float(entry.get())
    centimeters_val = inch_val *2.54
    result["text"]=str(centimeters_val)
title = Label(window,text="인치를 센티미터로 변환하는 프로그램")
title.grid(row=0,column=0,columnspan=2)
label = Label(window,text="인치를 입력하세요")
label.grid(row=1,column=0)
entry = Entry(window,fg="black")
entry.grid(row=1,column=1)
label2 = Label(window,text="반환결과")
label2.grid(row=2,column=0)
result = Label(window,text=" ")
result.grid(row=2,column=1)
bt = Button(window,text="변환!",command=do_convert)
bt.grid(row=3,column=1)

window.mainloop()