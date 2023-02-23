import turtle
ok = turtle.Turtle()
ok.pensize(10)
ok.color("black","yellow")

ok.begin_fill()
for i in range(5):
    ok.forward(200)
    ok.left(360/5)
ok.end_fill()

turtle.done()