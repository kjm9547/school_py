import turtle

t= turtle.Turtle()
a =100
t.speed(0)
for y in range(1,500,1):
    if y%50 ==0:
        a+=25
    for i in range(5):
        t.forward(a)
        t.left(-144)
    t.left(10)

turtle.mainloop()
turtle.bye()