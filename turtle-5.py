import turtle 
x = turtle.Turtle()

def cokgen(uzunluk, kenarSayisi,kalemKalinligi,disRenk,icrenk):
    x.pensize(kalemKalinligi)
    x.color(disRenk, icrenk)
    x.begin_fill()
    for i in range(kenarSayisi):
        x.forward(uzunluk)
        x.left(360/ kenarSayisi)
    x.end_fill()
    
def boslukBirak(mesafe):
    x.penup()
    x.forward(mesafe)
    x.pendown()

x.penup()
x.goto(-800,0)
x.pendown()

for i in range(3,8,1):
    cokgen(150,i,5,"black","yellow")
    boslukBirak(70 * i)
    
turtle.done()