import random
import turtle

t = turtle.Turtle()
t.shape("turtle")
r= random.Random()
t.speed(0)
for i in range(10):
    radius = r.randint(1,100)
    x = r.randint(-300,300)
    y=r.randint(-100,100)
    t.up()
    t.goto(x,y)
    t.down()
    t.circle(radius)

turtle.mainloop()
turtle.bye()

