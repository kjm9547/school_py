import turtle
t= turtle.Turtle()
t.shape("turtle")

s=turtle.textinput("","도형을 입력: ")
if s == "사각형":
    len = turtle.textinput("","가로: ")
    x=int(len)
    len = turtle.textinput("","세로: ")
    y=int(len)
    t.forward(x)
    t.left(90)
    t.forward(y)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(y)
    
    
if s == "원":
    len=turtle.textinput("","반지름을 입력: ")
    r=int(len)
    t.circle(r)
if s == "삼각형":
    len = turtle.textinput("","변의 길이 입력: ")
    len=int(len)
    t.left(60)
    t.forward(len)
    t.right(240)
    t.forward(len)
    t.left(120)
    t.forward(len)

turtle.mainloop()
turtle.bye()