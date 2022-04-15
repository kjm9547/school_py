import turtle
import random
t= turtle.Turtle()
r=random.Random()

color_list = ["red","orange","yellow","green","blue","indigo","purple"]
length = 5
i=0
t.speed(0)
turtle.bgcolor("black")
t.fillcolor("red")
t.begin_fill
t.end_fill
while True:
    num = r.randint(0,6)
    t.forward(length)
    t.color(color_list[num])
    t.left(89)
    length += 5
   

