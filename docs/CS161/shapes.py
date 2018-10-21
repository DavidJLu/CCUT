import turtle

def drawSun(pen,x,y,size):
  pen.setheading(0)
  pen.fillcolor("yellow")
  pen.penup()
  pen.goto(x,y)
  pen.pendown()
  pen.begin_fill()
  pen.circle(size)
  pen.end_fill()
  
def drawCloud(pen,x,y):
  pen.setheading(90)
  pen.fillcolor("white")
  pen.penup()
  pen.goto(x,y)
  pen.pendown()
  pen.color("white")
  for x in range(10):
    pen.begin_fill()
    pen.circle(25)
    pen.end_fill()
    pen.right(36)
    pen.forward(1)
  pen.setheading(90)  
 
 
def drawGrass(pen):
  pen.setheading(90)
  pen.fillcolor("#057203")
  pen.penup()
  pen.setheading(90)
  pen.goto(-400,-400)
  pen.begin_fill()

  for x in range(2):
    pen.forward(400)
    pen.right(90)
    pen.forward(800)
    pen.right(90)
  pen.end_fill()  
  
def drawBush(pen,x,y):
  pen.setheading(90)
  pen.fillcolor("darkgreen")
  pen.width(5)
  pen.penup()
  pen.goto(x,y)
  pen.pendown()

  pen.color("darkgreen")
  for x in range(10):
    pen.begin_fill()
    pen.circle(22)
    pen.right(36)
    pen.forward(1)
    pen.end_fill()
  pen.setheading(90)    


def drawPath(pen):
  pen.setheading(90)  
  pen.color(0,0,0)
  pen.fillcolor("#965000")
  pen.penup()
  pen.goto(-90,-400)
  pen.begin_fill()
  pen.pendown()
  pen.right(10)
  pen.forward(403)
  pen.right(80)
  pen.forward(40)
  pen.right(80)
  pen.forward(403)
  pen.right(80)
  pen.end_fill()
  pen.setheading(90)  

def drawFence(pen):
  pen.setheading(90)
  pen.color("#000000")  
  #fence
  pen.penup()
  pen.goto(-400,-200)
  pen.pendown()
  pen.setheading(90)

  #pen.left(50)
  pen.fillcolor("#734f03")
  pen.begin_fill()
  for x in range(25):
    pen.forward(100)
    pen.right(45)
    pen.forward(20)
    pen.right(90)
    pen.forward(20)
    pen.right(45)
    pen.forward(100)
    pen.left(90)
    pen.forward(4)
    pen.left(90)
  pen.end_fill()

  #handle
  pen.penup()
  pen.goto(47,-140)
  pen.pendown()
  pen.fillcolor("#b1bcb1")
  pen.begin_fill()
  pen.circle(7)
  pen.end_fill()
  pen.begin_fill()
  pen.fillcolor("#734f03")
  pen.penup()
  pen.goto(44,-140)
  pen.pendown()
  pen.circle(4)
  pen.end_fill()

  #hinges
  coord1 = [-50,-190]
  coord2 = [-50,-130]
  l = [coord1,coord2]
  for y in range(2):
    pen.penup()
    pen.goto(l[y])
    pen.fillcolor("#b1bcb1")
    pen.begin_fill()
    pen.pendown()
    for x in range (2):
      pen.forward(10)
      pen.right(90)
      pen.forward(15)
      pen.right(90)
    pen.end_fill()
  pen.setheading(90)    
  

def drawHouse(pen):
  pen.color(0,0,0)  
  pen.penup()
  pen.goto(-160,-20)
  pen.pendown()
  pen.setheading(90)
  pen.fillcolor("white")
  pen.begin_fill()
  pen.forward(150)
  roof1=pen.position()
  pen.right(90)
  pen.forward(300)
  roof2 = pen.position()
  pen.right(90)
  pen.forward(150)
  pen.right(90)
  pen.forward(300)
  pen.right(90)
  pen.end_fill()
  
  #roof
  pen.penup()
  pen.goto(roof1)
  pen.fillcolor("#f48342")
  pen.begin_fill()
  pen.pendown()
  pen.goto(-10,200)
  pen.goto(roof2)
  pen.goto(roof1)
  pen.end_fill()
  pen.setheading(90)


def drawDoor(pen,x,y):
  #door
  pen.penup()
  pen.goto(x,y)
  pen.fillcolor("#b40000")
  pen.begin_fill()
  pen.setheading(90)

  for x in range(2):
    pen.forward(50)
    pen.right(90)
    pen.forward(30)
    pen.right(90)

  pen.end_fill()

  #handle
  pen.fillcolor("yellow")
  pen.penup()
  pen.goto(x,y+20)
  pen.begin_fill()
  pen.circle(4)
  pen.end_fill()


def drawWindow(pen,x,y,shape):
  pen.width(4)
  pen.color("black")
  pen.fillcolor("lightblue")
  
  if shape=="square":
    pen.penup()
    pen.goto(x,y)
    pen.pendown()
    pen.begin_fill()

  
    for y in range(4):
      for x in range(4):
        pen.forward(20)
        pen.right(90)
      pen.left(90)
    pen.end_fill()
  else:
    pen.penup()
    pen.goto(x,y)
    pen.pendown()
    pen.backward(20)
    pen.right(90)
    pen.begin_fill()
    pen.circle(20)
    pen.end_fill()
    pen.goto(x,y)
    
    for x in range(2):
      pen.forward(20)
      pen.backward(40)
      pen.forward(20)
      pen.right(90)

