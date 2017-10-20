#StarColor.py
import turtle 

colors=['red', 'purple', 'blue',
        'green', 'orange', 'yellow']    # List

t = turtle.Turtle()
turtle.bgcolor('black')
t.color('green')
t.width(5)

for i in range(50):
    t.color(colors[i%6])  #  5 / 3 = 1 remainer 2 
    t.forward(150)        #  5 mod 3 = 2 
    t.right(144)

turtle.done()
