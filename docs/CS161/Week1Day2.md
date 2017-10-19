CS161 at CCUT Week 1: Day 2
======

Before we return to C++, let's play around with that Python example from last time and see how parts of the program work and what happens when we modify it a bit.

>Python is free and easy to get from the Python website: www.python.org
>So if you'd like to learn Python, go to the website's Downloads area and download and install Python 3 and the IDLE editor.
>
>Python is an interpreted language rather than a compiled one. IDLE is a program that's used to type and run our Python programs.
>
>You can test your installation by starting IDLE and running a simple program.
>Start IDLE and type `Print("Hello World")` and then press enter.

Python is a widely used *high-level programming language*, created by Guido van Rossum in 1991. Python is an interpreted language, and has a design philosophy that emphasizes code readability (notably using whitespace indentation to delimit code blocks rather than curly brackets or keywords). It also has a syntax that allows programmers to express concepts in fewer lines of code than might be used in languages such as C++ or Java.

In Python, `Turtle graphics` is a library that allows us to draw basic pictures. It's a great tool for introducing beginning programmers to programming concepts. You can find the documentation at [https://docs.python.org/3.2/library/turtle.html](https://docs.python.org/3.2/library/turtle.html)

Imagine a robotic turtle starting at (0, 0) in the x-y plane. After an `import turtle`, give it the command `turtle.forward(100)`, and it moves (on-screen!) 100 pixels in the direction it is facing, drawing a line as it moves. Give it the command `turtle.right(90)`, and it rotates in-place 90 degrees clockwise.

By combining together these and similar commands, we can draw shapes and pictures.

What do you think the following bit of code does?

``` Py
import turtle

t = turtle.Turtle()
turtle.bgcolor('black')
t.color('red')

t.forward(100)  # Draw foward 100 pixels
t.right(90)     # Rotate clockwise by 90 degrees

t.forward(100)
t.right(90)

t.forward(100)
t.right(90)

t.forward(100)
t.right(90)
```

Let's consider it line by line.

Remember, `import turtle` allows us to use the turtle graphics library's functions. Importing code that's already written is one of the coolest things about programming. If you program something interesting and useful, you can share it with other people or reuse it yourself. Some Python programmers built a *library* to help other programmers use turtle graphics even though turtle graphics are originally from the Logo programming language from the 1960s! So `import turtle` allows your program to use the code that those programmers wrote. Cool!

>As you should already know, this can be done in C++ too. Your professor has shown you how to import the iostream library so that you can get input from the keyboard and output to the screen. In C++ you type `#include <iostream>`. This allows you to use the code that someone else wrote in order to output `Hello World` to the screen with the statement `cout << "Hello World";`

The next line `t = turtle.Turtle()` declares the variable `t` to be a turtle. What this means is that we can use `t` to draw lines. Don't worry about this line of code for now.

The next two lines set the color of the background on the canvas and the color of the line drawn by our turtle. Again, don't worry too much about these lines. You can play around with their values and see how things change if you like. Try substituting a white background or a different color. You can find what color strings are recognized online, or you can specify the RGB as a comma separated tuple.

The next line `t.forward(100)  # Draw foward 100 pixels` is interesting. This line says to move the turtle 100 pixels forward, drawing a line along the way. The turtle starts out in the center of the canvas facing right by default.

The `#` specifies a comment. Anything after the `#` on this line will not be interpreted as code by the computer. Comments are useful to explain what is going on with the code written and why it was written this way. It's a way to document the code for people who look at the code in the future. This is an important thing to do, since we want to be able to maintain our programs.

`t.right(90)` tells our turtle to turn right 90 degrees.

The next 3 pairs of lines do the same as the last two lines we inspected. Draw a line 100 pixels then turn 90 degrees. This draws a square!

How would we modify this to make a hexagon (6 sided polygon)? Let's modify the program and try it together.

> Hint: Think about what angles you need for a hexagon.

Although these programs are not long, we might notice that some parts of our code looks a lot like other parts of our code. A principle that we try to follow when writing good programs is *do not repeat yourself*

> Don't Repeat Yourself (DRY)

In this case, there is a better solution using loops. A loop statement in programming allows us to execute some other statement a number of times.

The syntax of a loop in Python looks like this:
```py
for n in range(x):
  do a
  do b
```
This code will do `a` then `b` x number of times. Each time through the loop, `n`, which is called a counter, gets incremented by 1. The expression `range(x)` gives us an integer beginning with `0` and incrementing to `x-1` each time through the loop.

> Test it yourself if you have the IDLE running. Test the following code. What do you think will happen? What happens?

```py
for n in range(4):
  print(n)
```

Loops are the first excellent way to follow the DRY principle. They allow us to execute repetitive tasks with many fewer lines of code.

Notice that the print line of this code is indented. Python marks code blocks through white space (tabs, spaces, etc...). So the body of this loop, the statements which will get executed multiple times, is whatever is contained in the body. What happens with the following bit of code?

```py
for n in range(4):
  print("Hello")
print("World")
```

Again, notice that the second print statement is not indented. What do you tink will happen? What happens?

Let's take a look at the implementation of the square drawing program using a loop.

>In C++, the syntax for loops are a bit different but the semantics are basically the same. In fact, there are 3 ways to write a loop in C++. We'll take a look at these later.

Here are some other interesting Python turtle programs. Let's explore them together.

-------
You can download these Python programs here:

[NiceHexSpiral.py](NiceHexSpiral.py)
[Square.py](Square.py)
[SquareLoop.py](SquareLoop.py)
[Star.py](Star.py)
[StarColor.py](StarColor.py)
[Polygon.py](Polygon.py)
[PolygonSides.py](PolygonSides.py)




<!---
Okay let's get back to some C++

Concepts from C++ that you should already be familiar with:

basic data types:

declaring variables:

input and output with `cin` and `cout`.

Basic C++ program structure:

But what is a program?
-->
