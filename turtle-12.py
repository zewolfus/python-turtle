import turtle
a = turtle.Turtle()
a.color("red")

a.penup()
a.back(500)
a.pendown()

for i in range(4):
    a.forward(100)
    a.left(90)
    
turtle.done()