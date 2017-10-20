import turtle as tu
import random as rn
def draw_star(x, y, color, side):
    tu.color(color)
    tu.begin_fill()
    tu.penup()
    tu.goto(x, y)
    tu.pendown()
    for k in range(5):
        tu.forward(side)
        tu.right(144)
        tu.forward(side)
    tu.end_fill()
def random_length():
    return rn.randrange(5, 25)
def random_xy_coord():
    return rn.randrange(-290, 290), rn.randrange(-270, 270) 
tu.title('a star filled sky')
tu.bgcolor('black')
# optional ('normal' is default) ...
# values for speed are 'fastest' (no delay), 'fast', (delay 5ms),
# 'normal' (delay 10ms), 'slow' (delay 15ms), 'slowest' (delay 20ms)
tu.speed('fastest')
colors = ['red', 'orange', 'magenta', 'purple', 'green', 'blue', 'yellow', 'white']
# number of stars you want to show
stars = 50
for k in range(stars):
    color = rn.choice(colors)
    side = random_length()  # length of side
    x, y  = random_xy_coord()
    draw_star(x, y, color, side)
# keep showing until window corner x is clicked
tu.done()