import turtle

t= turtle.Turtle()
t.shape("turtle")

x1 = turtle.textinput("", "첫 번째 점의 X 좌표 x1: ")
y1 = turtle.textinput("", "첫 번째 점의 y 좌표 y1: ")

x2 = turtle.textinput("", "두 번째 점의 x 좌표 x2: ")
y2 = turtle.textinput("", "두 번째 점의 y 좌표 y2: ")

x1 =int(x1)
y1 =int(y1)
x2 =int(x2)
y2 =int(y2)

dist = ((x1-x2)**2 + (y1-y2)**2)**0.5
t.up()
t.goto(x1,y1)
t.down()
t.goto(x2,y2)
t.up()
t.write("두 점 사이의 거리는="+str(dist))

turtle.mainloop()
turtle.bye()