#Polygon.py
import turtle 

polygon = turtle.Turtle()

num_sides = 6
side_length = 100
pen_width = 3
color = 'orange'
angle = 360.0 / num_sides 

for i in range(num_sides):
    polygon.width(pen_width)
    polygon.color(color)
    polygon.forward(side_length)
    polygon.right(angle)
    
turtle.done()
