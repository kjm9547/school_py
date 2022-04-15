

from tkinter import mainloop
import turtle

t= turtle.Turtle()

position = []
t.shape("turtle")
x1 = int(turtle.textinput(" ","x1"))
y1 = int(turtle.textinput(" ","y1"))
x2 = int(turtle.textinput(" ","x2"))
y2 = int(turtle.textinput(" ","y2"))
x3= int(turtle.textinput(" ","x3"))
y3 = int(turtle.textinput(" ","y3"))
position.append(x1)
position.append(y1)
position.append(x2)
position.append(y2)
position.append(x3)
position.append(y3)

t.goto(position[0],position[1])
t.goto(position[2],position[3])
t.goto(position[4],position[5])
t.write("위치값은"+str(position[4]))

turtle.mainloop()
turtle.bye()