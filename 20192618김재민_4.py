import turtle
t= turtle.Turtle()
t.shape("turtle")

size = int(input("집의 크기는 얼마로 할까요?"))

t.forward(size)
t.right(90)
t.forward(size)
t.right(90)
t.forward(size)
t.right(90)
t.forward(size)

t.right(90)

t.forward(size)
t.left(120)
t.forward(size)
t.left(120)
t.forward(size)


new_size = float(size/3)
t.forward(new_size)
t.up()
t.goto(size,0)
t.down()
t.left(60)
t.forward(new_size)

box = float(new_size/2)
t.up()
t.goto(new_size,-box)
t.down()
t.left(60)
t.forward(new_size)
t.right(90)
t.forward(new_size)
t.right(90)
t.forward(new_size)
t.right(90)
t.forward(new_size)

turtle.mainloop()
turtle.bye()
