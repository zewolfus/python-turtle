import turtle
ok = turtle.Turtle()

ok.pensize(10)

ok.color("purple")
for i in range(4):
    ok.forward(200)
    ok.right(360/4)
ok.color("pink")
for c in range(3):
    ok.forward(200)
    ok.left(360/3)
turtle.done()