


import turtle

x = turtle.Turtle()

def kareCiz():
    for i in range(4):
        x.forward(250)
        x.left(360/4)
def ucgenCiz():
    for a in range(3):
        x.forward(250)
        x.left(360/3)
        
kareCiz()
ucgenCiz()
turtle.done()
