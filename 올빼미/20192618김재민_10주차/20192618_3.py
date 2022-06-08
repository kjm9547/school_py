from tkinter import*
import random

secret_number = random.randint(1, 100)

window = Tk()
def guess_number():
    guess = int(entry.get())
    if guess == secret_number:
        label["text"] ="축하합니다."
    elif guess < secret_number:
        label["text"] = "너무 낮아요!"
    else:
        label["text"] = "너무 높아요"
def reset():
    label["text"] = "1부터 100사이의 숫자를 입력하세요"
    entry.delete(0,END)
    global secret_number 
    secret_number = random.randint(1,100)

label = Label(window,text="1부터 100사이의 숫자를 추측하시오")
label.grid(row=0,column=0,columnspan=2)
entry = Entry(window,fg="black")
entry.grid(row=1,column=0,columnspan=2)
input_bt = Button(window,text="숫자를 입력",command=guess_number)
input_bt.grid(row=2,column=0)
restart_bt = Button(window,text="게임을 다시 실행",command=reset)
restart_bt.grid(row=2,column=1)
window.mainloop()