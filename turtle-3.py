
import turtle
x = turtle.Turtle()

def kareCiz(uzunluk, kenarRengi, icRengi, kalemKalinligi):
    x.color(kenarRengi, icRengi)
    x.pensize(kalemKalinligi)
    x.begin_fill()
    for i in range(4):
        x.forward(uzunluk)
        x.left(360/4)
    x.end_fill()    
def ucgenCiz(uzunluk, kenarRengi, icRengi, kalemKalinligi):
    x.color(kenarRengi, icRengi)
    x.pensize(kalemKalinligi)
    x.begin_fill()
    for a in range(3):
        x.forward(uzunluk)
        x.left(360/3)
    x.end_fill()
def  boslukBirak(mesafe):
    x.penup()
    x.forward(mesafe)
    x.pendown()    
kareCiz(200, "red", "yellow", 10)
boslukBirak(300)
ucgenCiz(250,"purple", "pink",5)

turtle.done()