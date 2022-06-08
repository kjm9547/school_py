from tkinter import *
import random

def change_image(x):
    y = random.randint(1,3)
    change1(x) 
    change2(y) 
    game(x,y) 

def change1(x):
    photo1 = PhotoImage(file=A[x])
    label1.configure(image=photo1)
    label1.image = photo1

def change2(x): 
    photo2 = PhotoImage(file=A[x])
    label3.configure(image=photo2)
    label3.image = photo2

def game(x,y):
    def win(): 
        label2.configure(text=">>>>>")
        label4.configure(text="사용자 승!")
    def lose(): 
        label2.configure(text="<<<<<")
        label4.configure(text="사용자 패배!")
    def draw(): 
        label2.configure(text="=====")
        label4.configure(text="비겼습니다!")

    if x==1: 
        if y==1:draw()
        elif y==2:lose()
        else:win()
    elif x==2: 
        if y==1:win()
        elif y==2:draw()
        else:lose()
    else:
        if y==1:lose()
        elif y==2:win()
        else:draw()

window = Tk()
font1 = ("굴림체",30,"bold") 
font2 = ("굴림체",20,"bold") 
A = {1:"C:/Users/최원석/Desktop/rock.png",2:"C:/Users/최원석/Desktop/scissors.png",3:"C:/Users/최원석/Desktop/paper.png"} #딕셔너리를 이용해 파일 경로를 저장해서 불러오기 편하게 해줌

photo1 = PhotoImage(file=A[3]) 
photo2 = PhotoImage(file=A[3]) 

label1 = Label(window, image=photo1)
label2 = Label(window, text = "=====",font=font1)
label3 = Label(window, image=photo2)
label1.grid(row=0, column=0)
label2.grid(row=0, column=1, padx=50)
label3.grid(row=0, column=2)

label4 = Label(window, text = "무승부!",font=font2,fg="green")
label4.grid(row=1, column=1)

button1 = Button(window,text="바위",command=lambda: change_image(1))
button2 = Button(window,text="보",command=lambda: change_image(2))
button3 = Button(window,text="가위",command=lambda: change_image(3))

button1.grid(row=2,column=0,ipadx=50)
button2.grid(row=2,column=1,ipadx=50)
button3.grid(row=2,column=2,ipadx=50)

window.mainloop()