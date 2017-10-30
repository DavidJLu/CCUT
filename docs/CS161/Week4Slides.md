---
presentation:
  # The "normal" size of the presentation, aspect ratio will be preserved
  # when the presentation is scaled to fit different resolutions. Can be
  # specified using percentage units.
  width: 960
  height: 700
  transition: 'slide'
---

<!-- slide data-background-video="../Portlandia.mp4" -->

<!-- slide -->
# CS161 at CCUT Week 4:

## Control Structures (If... else...)

And more turtle!

<!-- slide -->
Last week we were looking at this function and deciding whether it was (1) correct and (2) efficient :

```py
def isEven(value):
  numbers = list(range(0, 100))
  odd = False
  for num in range(0, 100):
    if odd:
      numbers.remove(num)
    odd = not odd
  if value in numbers:
    return True
  else:
    return False
```
And maybe (3) is it easy to understand?

<!-- slide -->
One of your classmates suggested we use the modulo operator `%` for a better solution.

```py
def isEven(value):
    if value % 2 == 0:
        return True
    else:
        return False
```
Is it correct, efficient, and easy to understand?

<!-- slide -->
Here we see a new structure we haven't discussed yet: the **conditional statement**.

<!-- slide -->
So far, our turtle programs, when run, execute *every* statement beginning from the top to the bottom, sometimes with a loop over a block of statements.

<!-- slide -->
### Conditional Statement
The `if` keyword allows the program we write to make a decision during runtime.

Syntax:
```py
if {boolean expression}:
  Some statements
  Some more statements in the block

Statements outside of the block
```

<!-- slide -->
#### If... Else...

We can also specify some behavior if the boolean expression is false:

```py
if {boolean expression}:
  Some statements
else:
  Some alternate behavior
```

<!-- slide -->



<!-- slide -->
```python
import turtle
t = turtle.Pen()
t.speed(20)          # Set turtle drawing speed

colors=['deep sky blue', 'orange red', 'sea green', 'dark slate gray', 'cyan', 'purple',
        'deep pink', 'navy', 'lavender', 'aquamarine', 'pink', 'gold']

sides = int(turtle.numinput("Number of sides", "How many spiral sides?", 4, 1, 12))

for m in range(0, 75):
    t.pencolor(colors[m % len(sides)])
    t.left(360/sides + 20/sides)
    t.width(m//25+1)        # // is floor division
    t.penup()
    t.forward(m * (20/sides)) # Scale for number of sides
    t.pendown()
    if (m % 2 == 0):     # Draw a rosette at each even corner
        for n in range(sides):
            t.circle(m/3)
            t.right(360/sides)
    else:                # Draw a polygon at each odd corner
        for n in range(sides):
            t.forward(m)
            t.right(360/sides)
t.exitonclick()
```


<!-- slide data-background-video="../Duke.mp4" data-background-video-loop=true -->
<div style="color:#5AFF0A"> I look forward to seeing all of you next spring!!</div>
