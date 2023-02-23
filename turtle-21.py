import turtle, random
renkler = ["red", "green", "blue", "yellow" ,"orange", "cyan", "black","purple"]

x = turtle.Turtle()
x.pensize(5)
for i in range(8):
    uretilenSAyi = random.randint(0,len(renkler)-1)
    x.color(renkler[uretilenSAyi])
    x.fd(200)
    x.bk(200)
    x.lt(360 / 8)
    
turtle.done()