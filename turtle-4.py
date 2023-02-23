

import turtle

x = turtle.Turtle()

def kareCiz(uzunluk, kenarRengi, icrenk, kalemKalinlik):
    x.color(kenarRengi ,icrenk)
    x.pensize(kalemKalinlik)
    x.begin_fill()
    for i in range(4):
        x.forward(uzunluk)
        x.left(360/4)
    x.end_fill()
def ucgenCiz(uzunluk, kenarRengi, icRenk, kalemKalinlik):
    x.color(kenarRengi , icRenk)
    x.pensize(kalemKalinlik)
    x.begin_fill()
    for a in range(3):
        x.forward(uzunluk)
        x.left(360/3)
    x.end_fill()
def boslukBirak(mesafe):
    x.penup()
    x.forward(mesafe)
    x.pendown()
    
x.left(180)
boslukBirak(600)
x.left(180)

for c in range(3):
    kareCiz(150, "black", "yellow", 10)
    boslukBirak(200)
    ucgenCiz(150,"black","red",5)
    boslukBirak(200)
    
turtle.done()