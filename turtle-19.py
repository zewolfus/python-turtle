import turtle
k = turtle.Turtle()
k.pensize(3)

uzunluk = 100

k.color("black","yellow")
k.begin_fill()
for i in range(3):
    k.forward(uzunluk)
    k.left(360/3)
k.end_fill()

k.penup()
k.forward(150)
k.pendown()

k.color("blue","red")
k.begin_fill()
for i in range(4):
    k.forward(uzunluk)
    k.left(360/4)
k.end_fill()

turtle.done()
