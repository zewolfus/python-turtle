import turtle

x = turtle.Turtle()

def kareCiz():
    x.color('black','red')
    x.pensize(5)
    x.begin_fill()
    for i in range(4):
        x.forward(250)
        x.left(360/4)
    x.end_fill()
def ucgenCiz():
    x.color("green","purple")
    x.pensize(5)
    x.begin_fill()
    for a in range(3):
        x.forward(250)
        x.left(360/3)
    x.end_fill()
    
kareCiz()
ucgenCiz()

turtle.done()