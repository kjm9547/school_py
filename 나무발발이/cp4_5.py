from telnetlib import X3PAD
import turtle

t= turtle.Turtle()
t.shape("turtle")
t.speed(0)
position = []


x1 =int(input("x1:"))
y1 =int(input("Y1:"))


x2 =int(input("x2:"))
y2 =int(input("y2:"))

x3 =int(input("x3:"))
y3 =int(input("y3:"))

position.append(x1)
position.append(y1)

position.append(x2)
position.append(y2)

position.append(x3)
position.append(y3)



t.goto(position[0],position[1])



t.goto(position[2],position[3])

t.goto(position[4],position[5])



turtle.mainloop()
turtle.bye()