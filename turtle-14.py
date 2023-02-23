import turtle

a = turtle.Turtle()
a.speed(0)
a.penup()
a.back(500)
a.pendown()
a.pensize(5)

for c in range(10):
    for i in range(3):
        a.forward(50)
        a.right(120)
    a.penup()
    a.forward(75)
    a.pendown()
turtle.done()