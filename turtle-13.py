import turtle
a = turtle.Turtle()
a.color("blue")
a.penup()
a.back(500)
a.pendown()
a.pensize(10)
for i in range(8):
    a.forward(50)
    a.penup()
    a.forward(50)
    a.pendown()
turtle.done()