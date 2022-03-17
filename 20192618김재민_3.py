import turtle

t= turtle.Turtle()
t.shape("turtle")
side = int(input("한 변의 길이는?"))
angle = 90

t.forward(side)
t.right(angle)

t.forward(side)
t.right(angle)

t.forward(side)
t.right(angle)

t.forward(side)
t.right(angle)

t.left(angle)
t.left(angle)

t.forward(side)
t.left(angle)
t.forward(side)
t.left(angle)
t.forward(side)
t.left(angle)
t.forward(side)

t.forward(side)
t.left(angle)
t.forward(side)
t.left(angle)
t.forward(side)
t.left(angle)
t.forward(side)

t.forward(side)
t.left(angle)
t.forward(side)
t.left(angle)
t.forward(side)
t.left(angle)
t.forward(side)

turtle.mainloop()
turtle.bye()
