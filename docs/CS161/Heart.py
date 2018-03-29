#David Lu

from turtle import * 	# Makes code look a bit cleaner

def curvemove():     	# A function!
    for i in range(200):
        right(1)
        forward(1)
        
color('red','pink')        
begin_fill()
left(140)
forward(111.65)
curvemove()
left(120)
curvemove()
forward(111.65)
end_fill()
exitonclick()			# Exit on click once done.

