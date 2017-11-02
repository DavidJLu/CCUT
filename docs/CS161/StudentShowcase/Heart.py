
#heart

from turtle import *
from time import sleep

def go_to(x, y):
   up()
   goto(x, y)
   down()


def big_Circle(size):  
   speed(10)
   for i in range(150):
       forward(size)
       right(0.3)

def small_Circle(size):  
   speed(10)
   for i in range(210):
       forward(size)
       right(0.786)

def line(size):
   speed(10)
   forward(51*size)

def heart( x, y, size):
   go_to(x, y)
   left(150)
   begin_fill()
   line(size)
   big_Circle(size)
   small_Circle(size)
   left(120)
   small_Circle(size)
   big_Circle(size)
   line(size)
   end_fill()

def arrow():
   pensize(10)
   setheading(0)
   go_to(-400, 0)
   left(15)
   forward(150)
   go_to(339, 178)
   forward(150)

def arrowHead():
   pensize(1)
   speed(10)
   color('red', 'red')
   begin_fill()
   left(120)
   forward(20)
   right(150)
   forward(35)
   right(120)
   forward(35)
   right(150)
   forward(20)
   end_fill()



pensize(2)
color('red', 'pink')
#getscreen().tracer(30, 0) 
heart(200, 0, 1)          
setheading(0)             
heart(-80, -100, 1.5)     
arrow()                   
arrowHead()               
go_to(400, -300)
write("SJ最可爱", move=True, align="left", font=("宋体", 30, "normal"))
exitonclick()


