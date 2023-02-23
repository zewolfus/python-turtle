from turtle import *

def geri(mesafe):
    penup()
    back(mesafe)
    pendown()
def ileri(mesafe):
    penup()
    format(mesafe)
    pendown()
def yukari(mesafe):
    penup()
    left(90)
    forward(mesafe)
    right(90)
    pendown()
def asagi(mesafe):
    penup()
    forward(mesafe)
    left(90)
    pendown()
def cokgen(uzunluk, kenarSayi, kalilnlik, disRenk, icRenk):
    pensize(kalilnlik)
    color(disRenk, icRenk)
    begin_fill()
    for a in range(kenarSayi):
        forward(uzunluk)
        left(360 / kenarSayi)
    end_fill()
bgcolor("purple")
speed(0)
penup()
goto(-300, -400)
pendown()
cokgen(400,3,5,"green","orange")
asagi(200)
ileri(50)
cokgen(75,6,3,"black","white")
ileri(220)
cokgen(75,6,3,"black","white")
geri(150)
asagi(200)
cokgen(150,4,5,"black","blue")
done()