#SquareLoop.py
import turtle 

t = turtle.Turtle()
turtle.bgcolor("white")
t.color("red")

# Loop 4 times. Everything I want to repeat is 
# *indented* by four spaces.
for i in range(6):
    t.forward(100)
    t.right(90)

turtle.done()
