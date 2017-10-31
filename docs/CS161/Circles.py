#David Lu
import turtle
 
t=turtle.Turtle()
t.screen.bgcolor("white")
colors=["red","green","purple"]
 
for x in range(100):
    t.circle(x)
    t.color(colors[x%3])
    t.left(60)
 
t.screen.exitonclick()

