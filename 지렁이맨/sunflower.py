import turtle

t= turtle.Turtle()
t.speed(0)
t.color("red","yellow")
t.begin_fill()
while True:
    t.forward(200)
    t.left(170)
    if abs(t.pos())<1:
        break
t.end_fill()

turtle.mainloop()
turtle.bye()