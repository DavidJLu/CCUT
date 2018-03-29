#ChineseNationalFlag.py
import turtle

t = turtle.Turtle()
turtle.bgcolor('black')
t.color('red')

width = -350
height =300
t.penup()
t.goto(width,height)
t.pendown()
t.begin_fill()
t.fillcolor('red')
t.forward(700)
t.right(90)
t.forward(400)
t.right(90)
t.forward(700)
t.right(90)
t.forward(400)
t.right(90)
t.end_fill()

width = -290
height = 225
t.penup()
t.goto(width,height)
t.pendown()
t.color('yellow')
t.begin_fill()
t.fillcolor('yellow')
for i in range(5):
    t.forward(120)
    t.right(144)
t.end_fill()

width = -100
height = 260
t.penup()
t.goto(width,height)
t.pendown()
t.color('yellow')
t.begin_fill()
t.fillcolor('yellow')
t.right(168)
for i in range(5):
    t.forward(40)
    t.right(144)
t.end_fill()

width = -100
height = 218
t.penup()
t.goto(width,height)
t.pendown()
t.color('yellow')
t.begin_fill()
t.fillcolor('yellow')
t.right(525)
for i in range(5):
    t.forward(40)
    t.right(144)
t.end_fill()

width = -100
height = 167
t.penup()
t.goto(width,height)
t.pendown()
t.color('yellow')
t.begin_fill()
t.fillcolor('yellow')
t.right(27)
for i in range(5):
    t.forward(40)
    t.right(144)
t.end_fill()

width = -100
height = 117
t.penup()
t.goto(width,height)
t.pendown()
t.color('yellow')
t.begin_fill()
t.fillcolor('yellow')
t.right(168)
for i in range(5):
    t.forward(40)
    t.right(144)
t.end_fill()

width = -420
height = -190
t.penup()
t.goto(width,height)
t.pendown()
t.color('yellow')
t.width(10)
t.left(78)
t.forward(150)

width = -270
height = -350
t.penup()
t.goto(width,height)
t.pendown()

def curvemove():
    for i in range(200):
        t.right(1)
        t.forward(1)

t.color('red')
t.width(1)
t.begin_fill()
t.fillcolor('red')
t.left(230)
t.forward(111.65)
curvemove()
t.left(120)
curvemove()
t.forward(111.65)
t.end_fill()

width = -10
height = -190
t.penup()
t.goto(width,height)
t.pendown()
t.color('yellow')
t.width(10)
t.right(40)
t.forward(100)
t.left(90)
t.forward(150)
t.left(90)
t.forward(100)

width = 20
height = -190
t.penup()
t.goto(width,height)
t.pendown()
t.right(90)
t.forward(150)
width = 20
height = -265
t.penup()
t.goto(width,height)
t.pendown()
t.left(90)
t.forward(100)
width = 120
height = -190
t.penup()
t.goto(width,height)
t.pendown()
t.right(90)
t.forward(150)

width = 150
height = -190
t.penup()
t.goto(width,height)
t.pendown()
t.forward(150)

width = 180
height = -190
t.penup()
t.goto(width,height)
t.pendown()
t.forward(150)
width = 180
height = -190
t.penup()
t.goto(width,height)
t.pendown()
t.left(33.7)
t.forward(180)
width = 280
height = -190
t.penup()
t.goto(width,height)
t.pendown()
t.right(34)
t.forward(150)

width = 360
height = -190
t.penup()
t.goto(width,height)
t.pendown()
t.right(18.4)
t.forward(158.1)
width = 360
height = -190
t.penup()
t.goto(width,height)
t.pendown()
t.left(36.8)
t.forward(158.1)
width = 335
height = -265
t.penup()
t.goto(width,height)
t.pendown()
t.left(71.6)
t.forward(50)

turtle.exitonclick()
