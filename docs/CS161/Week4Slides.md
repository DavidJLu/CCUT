---
presentation:
  # The "normal" size of the presentation, aspect ratio will be preserved
  # when the presentation is scaled to fit different resolutions. Can be
  # specified using percentage units.
  width: 960
  height: 700
  transition: 'slide'
---

<!-- slide -->
```python {cmd=true}
import turtle
t = turtle.Pen()
t.speed(20)          # Set turtle drawing speed

colors=['deep sky blue', 'orange red', 'sea green', 'dark slate gray', 'cyan', 'purple',
        'deep pink', 'navy', 'lavender', 'aquamarine', 'pink', 'gold']
#sides = int(turtle.numinput("Number of sides", "How many spiral sides?", 4, 1, 12))
sides = 7

for m in range(0, 75):
    t.pencolor(colors[m % sides])
    t.left(360/sides + 20/sides)
    t.width(m//25+1)        # // is floor division
    t.penup()
    t.forward(m*20/sides) # Scale for number of sides
    t.pendown()
    if (m % 2 == 0):     # Draw a rosette at each even corner
        for n in range(sides):
            t.circle(m/3)
            t.right(360/sides)
    else:                # Draw a polygon at each odd corner
        for n in range(sides):
            t.forward(m)
            t.right(360/sides)

```
