#PolygonSides.py
import turtle 

shape = turtle.Turtle()

num_sides = int(input("How many sides do you want on your shape?"))

#num_sides = 6
side_length = 40
pen_width = 3
color = 'orange'
angle = 360.0 / num_sides 

for i in range(num_sides):
    shape.width(pen_width)
    shape.color(color)
    shape.forward(side_length)
    shape.right(angle)
    
turtle.done()
