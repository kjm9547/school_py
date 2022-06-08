import turtle

t = turtle.Turtle()

t.shape("turtle")
t.speed(0)


color1= turtle.textinput("", "색상#1")
color2 = turtle.textinput("", "색상#2")
color3 = turtle.textinput("", "색상#3")

c_list = []
c_list.append(color1)
c_list.append(color2)
c_list.append(color3)

t.fillcolor(c_list[0])
t.begin_fill()
t.circle(50)
t.end_fill()

t.up()
t.goto(100,0)
t.down()

t.fillcolor(c_list[1])
t.begin_fill()
t.circle(50)
t.end_fill()

t.up()
t.goto(200,0)
t.down()
t.fillcolor(c_list[2])
t.begin_fill()
t.circle(50)
t.end_fill()

turtle.mainloop()
turtle.bye()