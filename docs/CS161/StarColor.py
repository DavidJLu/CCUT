#StarColor.py
import turtle 

colors=['red', 'purple', 'blue',
        'green', 'orange', 'yellow']

t = turtle.Turtle()
turtle.bgcolor('black')
t.color('green')
t.width(5)

for i in range(50):
    t.color(colors[i%6])
    t.forward(150)
    t.right(144)

turtle.done()
