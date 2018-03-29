import turtle
t = turtle.Turtle()
turtle.bgcolor("#FFFFFF")
t.color("#000000")
t.width(10)
t.color("blue") 
t.penup() 
t.goto(-220,-50)
t.pendown() 
t.circle(90)  
 
t.color("black")
t.penup()
t.goto(0,-50)
t.pendown()
t.circle(90)
 
t.color("red")
t.penup()
t.goto(220,-50)
t.pendown()
t.circle(90)
 
t.color("yellow")
t.penup()
t.goto(-110,-150)
t.pendown()
t.circle(90)
 
t.color("green")
t.penup()
t.goto(110,-150)
t.pendown()
t.circle(90)

turtle.exitonclick()

