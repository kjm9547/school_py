import turtle

t= turtle.Turtle()

angle = int(turtle.textinput("","몇 각형 입니까?"))

for i in range(0,angle,1):
    t.forward(100)
    t.left(360/angle)

