import math
import turtle

t=turtle.Turtle()
for i in range(360):
    sine = math.sin(3.14*i/180.0)
    t.goto(i,sine*100)