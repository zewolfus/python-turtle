
import turtle

t = turtle.Turtle()

outer_side=200
width=20 
inner_side=outer_side-width
inner_triangle_side=inner_side/2 - 2*width


t.fillcolor("blue") 

t.begin_fill() #
t.backward(width) 
t.left(60) 
t.forward(outer_side) 

t.right(120) 
t.forward(outer_side)
t.right(120)
t.forward(width)



t.right(60)
t.forward(inner_side/2)
t.left(60)
t.forward(inner_side/2 - width)
t.left(60)
t.forward(inner_side/2)

t.end_fill()


t.left(180)
t.penup()

t.forward(inner_side/2 + width)


t.fillcolor("white")

t.begin_fill()
t.pendown()

t.forward(inner_triangle_side) 
t.right(120)
t.forward(inner_triangle_side)
t.right(120)
t.forward(inner_triangle_side)
t.end_fill()

turtle.done()