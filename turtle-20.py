import turtle

renkler = ["red","green","blue"]
uzunluk = 200
kenarSAyisi = 4
kalemKalinligi = 5
turtle.pensize(kalemKalinligi)
for i in range(3):
    turtle.color("black",renkler[i])
    turtle.begin_fill()
    for a in range(kenarSAyisi):
        turtle.fd(uzunluk)
        turtle.lt(360 / kenarSAyisi)
    turtle.end_fill()
    turtle.penup()
    turtle.fd(250)
    turtle.pendown()
turtle.done()