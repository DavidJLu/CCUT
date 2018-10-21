#import turtle
from shapes import *

pen = turtle.Turtle()
pen.speed(0)
pen.color(0,0,0)
wn = turtle.Screen()
wn.bgcolor("#42caf4")

drawGrass(pen)
drawBush(pen,120,35)
drawBush(pen,-200,25)
drawCloud(pen,75,160)
drawCloud(pen,130,210)
drawCloud(pen,230,230)
drawSun(pen,-200,160,70)
drawCloud(pen,-230,140)
drawPath(pen)
drawHouse(pen)
drawDoor(pen,-25,-20)
drawWindow(pen,-10,100,"circle")
drawFence(pen)
drawWindow(pen,-95,15,"square")
drawWindow(pen,-95,100,"square")
drawWindow(pen,75,15,"square")
drawWindow(pen,75,100,"square")

turtle.exitonclick()
