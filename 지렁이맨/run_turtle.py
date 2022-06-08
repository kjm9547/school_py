import turtle

t= turtle.Turtle()

for i in range(20):
    t.forward(100)
    if i%2==0:
        t.right(90)
    elif i%2 ==1:
        t.left(90)
    t.forward(20)
    if i%2==0:
        t.right(90)
    elif i%2 ==1:
        t.left(90)