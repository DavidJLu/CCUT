---
presentation:
  # The "normal" size of the presentation, aspect ratio will be preserved
  # when the presentation is scaled to fit different resolutions. Can be
  # specified using percentage units.
  width: 1280
  height: 740
  transition: 'slide'
---


<!-- slide -->
# https://codewith.mu/

<!-- slide -->
Problem solving with computers:

Input Problem $\to$ Calculate Solution $\to$ Output Answer

* Example: Determine whether a given number is odd or even.
1. Input number
2. Use arithmetic to determine if the number is odd or even.
3. Output 'Even' if the number is even and 'Odd' if the number is odd

<!-- slide -->
Python Basics:

* Output (writing to the screen)
```py
print()
```
* Input
```py
input ()
```
* Variables
```py
name = "David"
number = 123
floatingPoint = 321.123
test = False
```

<!-- slide -->
Python Lists
(https://docs.python.org/3/tutorial/datastructures.html)
```py
list = []  # Empty list
games = ["Starcraft", "Dota", "Overwatch"]
firstTenPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

print(games[0]) # Index first item of a list

print(len(firstTenPrimes)) # len() gives the length of the argument you give it

print(sorted(games))  #sorted() gives you a sorted version of a list

games.sort() # Sorts your list

games.remove("Overwatch")  # Removes an item by match from list

games.append("League of Legends") # Adds an item to the end of a list
```
<!-- slide -->
Python Control Structures:
(https://docs.python.org/3/tutorial/controlflow.html)

```py
if x == y:
  print("Do something if x equals y")
elif x == z:
  print("Do something if x does not equal y but equals z")
else:
  print("Do something else")
```

<!-- slide -->

More Python Control Structures: Loops
(https://docs.python.org/3/tutorial/controlflow.html#for-statements)
```py
while True:
  print("This loops forever")
```
```py
for x in range(10):
  print(x)  # prints 0 through 9
```
```py
list = [1, 3, 5]
sum = 0
for x in list:
  sum = sum + x
print(sum)  # prints the sum of the ints in list
```

<!-- slide -->
Turtle Graphics
(https://docs.python.org/3/library/turtle.html)
You can draw stuff with Python and turtle graphics using code

```py
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
```

<!-- slide -->
Python Functions
How to reuse code

```py
def fahrenheit(temp_celsius):
    return (temp_celsius * 9 / 5) + 32

temp = 24
print(fahrenheit(temp))
```
