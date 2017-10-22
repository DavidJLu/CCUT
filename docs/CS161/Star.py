#Star.py
#David Lu
import turtle 

t = turtle.Turtle()
turtle.bgcolor('white')
t.color('green')
t.width(5)

for i in range(50):
    t.forward(150)
    t.right(144)		# What kind of shape is drawn if we turn right 144 degrees?

turtle.exitonclick()
