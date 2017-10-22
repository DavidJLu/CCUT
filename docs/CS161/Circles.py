#David Lu
from turtle import Turtle
 
t=Turtle()
t.screen.bgcolor("white")
colors=["red","green","purple"]
#t.screen.tracer(0,0)
 
for x in range(100):
    t.circle(x)
    t.color(colors[x%3])
    t.left(60)
 
t.screen.exitonclick()
t.screen.mainloop()
