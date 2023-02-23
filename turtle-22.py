from turtle import *

def cemberCiz(cap, kenarRengi,icRengi, kalinlik):
    pensize(kalinlik)
    color(kenarRengi, icRengi)
    begin_fill()
    circle(cap)
    end_fill()
def bosluk_birak(mesafe):
    penup()
    fd(mesafe)
    pendown()
    
for i in range(4):
    cemberCiz(100, "black","purple",5)
    bosluk_birak(150)
    
done()