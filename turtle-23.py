from turtle import *

def geriyeBosluk(mesafe):
    penup()
    back(mesafe)
    pendown()
def ileriyeBosluk(mesafe):
    penup()
    forward(mesafe)
    pendown()
def yukariBosluk(mesafe):
    penup()
    left(90)
    forward(mesafe)
    right(90)
    pendown()
def asagiBosluk(mesafe):
    penup()
    right(90)
    forward(mesafe)
    left(90)
    pendown()
def cokgen(uzunluk,kenarSayisi,kalinlik,disRenk,icRenk):
    pensize(kalinlik)
    color(disRenk, icRenk)
    begin_fill()
    for a in range(kenarSayisi):
        forward(uzunluk)
        left(360 / kenarSayisi)
    end_fill()
    
geriyeBosluk(600)
baslangicX = xcor()
baslangicY = ycor()
for i in range(3):
    cokgen(200,3,5,"black","pink")
    asagiBosluk(200)
penup()
goto(baslangicX, baslangicY)
pendown()

ileriyeBosluk(300)
baslangicX = xcor()
baslangicY = ycor()
for i in range(3):
    cokgen(150,4,5,"red","cyan")
    asagiBosluk(200)
penup()
goto(baslangicX, baslangicY)
pendown()
done()