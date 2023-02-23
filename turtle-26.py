from turtle import *
pensize(3)
speed(5)
color("purple")
for i in range(36):
    forward(100)
    backward(100)
    left(10)
color("black")
setpos(100,100)
for i in range(36):
    forward(100)
    backward(100)
    left(10)
color("green")
goto(-100,100)
for i in range(36):
    forward(100)
    backward(100)
    left(10)
color("blue")
goto(-100,-100)
for i in range(36):
    forward(100)
    backward(100)
    left(10)
color("yellow")
goto(100,-100)
for i in range(36):
    forward(100)
    backward(100)
    left(10)
done()