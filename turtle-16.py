import turtle
cizici = turtle.Turtle()
cizici.penup()
cizici.left(180)
cizici.forward(400)
cizici.left(180)
cizici.pendown()
cizici.pensize(5)
for c in range(4):
    cizici.circle(100)
    cizici.penup()
    cizici.forward(150)
    cizici.pendown()
turtle.done()