import turtle

t= turtle.Turtle()
t.shape("turtle")
radius = 50

t.speed(0)
t.circle(radius)
t.up()
t.goto(100,0)
t.down()
radius+=20
t.circle(radius)
t.up()
t.goto(200,0)
t.down()
radius+=20
t.circle(radius)
turtle.mainloop()
turtle.bye()