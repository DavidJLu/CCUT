#PolygonSides.py
'''
David Lu
This is a block comment
'''
import turtle 

shape = turtle.Turtle()

num_sides = int(input("How many sides do you want on your shape?"))

#num_sides = 6  						# We don't need this line anymore!
side_length = 200/ (num_sides * .5)		# What does this do?
pen_width = 3
color = 'orange'
angle = 360.0 / num_sides 

for i in range(num_sides):
    shape.width(pen_width)
    shape.color(color)
    shape.forward(side_length)
    shape.right(angle)
    
turtle.exitonclick()
