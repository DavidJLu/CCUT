#Spiralgraph.py
import turtle   
colors=['red', 'purple', 'blue',
        'green', 'yellow', 'orange']
t=turtle.Pen()
turtle.bgcolor('white')
for x in range(360):
    t.pencolor(colors[x%6])
    #t.width(x/100+1)
    t.forward(100)        
    t.left(123)
