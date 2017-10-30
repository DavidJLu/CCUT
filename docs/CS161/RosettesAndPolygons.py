# RosettesAndPolygons.py

import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(40)          # Set turtle drawing speed

colors=['deep sky blue', 'orange red', 'green', 'yellow', 'cyan', 'purple',
        'deep pink', 'navy', 'lavender', 'aquamarine', 'pink', 'gold']
sides = int(turtle.numinput("Number of sides", "How many spiral sides?", 4, 1, 12))

for m in range(0, 120):
    t.pencolor(colors[m % sides])
    t.left(360/sides + 20/sides)
    t.width(m//25+1)        # // is floor division
    t.penup()
    t.forward(m*20/(1.2*sides)) # Scale for number of sides
    t.pendown()
    if (m % 2 == 0):     # Draw a rosette at each even corner
        for n in range(sides):
            t.circle(m/3)
            t.right(360/sides)
    else:                # Draw a polygon at each odd corner
        for n in range(sides):
            t.forward(m/2)
            t.right(360/sides)

turtle.exitonclick()
