import turtle

from setuptools import Command
t= turtle.Turtle()

t.width(3)
t.shape("turtle")
t.shapesize(3,3)

while True:
    Command = input("명령을 입력하시오: ")
    if Command == "1":
        t.left(90)
        t.forward(100)
    if Command == "r":
        t.right(90)
        t.forward(100)
    if Command == "q" or Command == "quit": 
        print("게임이 종료됬습니다.")
        break

turtle.mainloop()
turtle.bye()