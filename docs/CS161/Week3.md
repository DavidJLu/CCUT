#CS161 at CCUT Week 3: Programming Review: Python and Turtle

We've been using the Python IDE called IDLE to write and run programs (you can download it at https://www.python.org). It contains a python interpreter and text editor.

There are two ways to use IDLE. First, we can just start typing in Python commands. For instance, recall that on the first day of class, we opened up IDLE and typed in `print("Hello World")` and pressed enter. The output Hello World is immediately given.  

The second way to use IDLE is to create a file with a Python program in it. Once the program has been written, we can run or execute the program contained in the file. To create a new file or open a saved file, the options are in the IDLE menu bar under `File`.

A Python program is a file with a `.py` extension. It contains Python code, and as we've seen so far, it begins at the top of the file and executes lines of code in order.

A program is a sequence of commands to the computer, telling it what to do. Our job as programmers is to tell the computer step by step how to do some task we'd like the computer to do or solve a problem we'd like the computer to solve.

We've seen a number of different types of Python commands and statements. Here is a short review:

**Variables**: Variables can be used to hold values. We can declare a variable and assign it a value with the following syntax:
`var = 5`

This assigns the variable `var` the integer type value `5`. Remember that `5` and `"5"` are not the same type of values.

Remember to use variable names that will help you understand the purpose of your variable.

**Lists**: A list in python is an ordered collection of values. We can declare a variable for a list in the following way:

`colors = ["red", "blue", "green"]`

The list `colors` contains 3 values. The first is a character string `"red"`, the second `"blue"`, and the third `"green"`.

We can access an element of the list using `colors[n]`, where `n` is the nth - 1 item in the list. So `colors[1]` will access the value `"blue"`

Look at the python documentation to see how you can add or delete items from a list. (https://docs.python.org/3.7/tutorial/datastructures.html#more-on-lists)

**Comments**: Code comments, which are ignored when running the program are important to help you remember and understand your code.

Single line comments begin with `#`

Multiple line comments are surrounded by `""" Comment """`

**Operations**: Arithmetic operators such as `+`, `-`, `*`, `/` work mostly as you expect them to. Try them out with different data types and see what happens.

**Loops**: The idea of looping is important because it's a common way a computer can automate a repetitive task.

We saw that with the `for` loop we can execute a set of statements, once for each item in a list or range.

Look at the example programs from last week to see some `for` loop syntax.


-------



![House](House.png)

### In-class Group Exercise:

I would like everyone to have some practice designing a program, programming, and seeing the results of their own program in class.

>Exercise:
>Form a small group. Your task is to discuss with your group, design, and write a turtle program that draws a picture. It cannot be something I've shown you, but it can be very similar. If you forgot what you can do with turtle in Python, there is a list of commands below. You can also look it up on the python turtle documentation website: https://docs.python.org/3.7/library/turtle.html
>
>Each person in the group should have a chance to type at the keyboard.
>

Programming is a creative exercise. It's good practice to explore and modify someone else's program, but you should also be able to create your own program. Try to think of something new. *Don't just copy or memorize other people's code.*

Open IDLE and click on `file` to bring the drop down menu and click `new file`. This will open a text editor in which you can write your program.

Your program should contain the following 5 lines of code:

```py
import turtle
t = turtle.Turtle()
turtle.bgcolor("#FFFFFF")
t.color("#000000")

#---> Your code here <---

turtle.exitonclick()
```

Recall that the first line allows you to use the functions in the Turtle library. The second line assigns the variable `t` to be a turtle. The third line sets the background color to white. The fourth line sets the color that the turtle draws. `#000000` is `black`. The last line keeps your drawing open after it is done until you click the screen.

Remember that color codes begin with `#` and use a six digit hexadecimal number, the first two indicating the saturation of red, the next two green, and the last two blue. So very red will be `#FF0000`. You can also use some English color names such as `white`, `black`, `red`, `purple`, `yellow`, `green`, `blue`, and so on. You should experiment with colors and color codes.

Below you will find a list of statements patterns that you are allowed to use. You will generally need to first assign values to the variables before you can use the statements. Or you can replace the variables directly with numbers.

* `t.forward(x)`
Moves the turtle foward `x` pixels in the direction it's facing. `x` should be an int or float.

* `t.right(x)`
Turns the turtle `x` degrees right. `x` should be an int or float

* `t.left(x)`
Turns the turtle `x` degrees left.

* `t.width(x)`
Sets the width of the drawn line to `x` pixels.

* `t.color(x)`
Sets the color of the drawn line to `x`. `x` must be a color code or a color string.

* `t.fillcolor(x)`
  `t.begin_fill()`

  ``---> Your code here <---``

  `t.end_fill()`
Sets the fill color and fills in a shape that's drawn between the begin_fill() and end_fill() statements with that color.

* `t.penup()`
Turtle will not draw when it moves until pendown() statement is executed.

* `t.pendown()`
Turtle will draw a line when it moves. This happens by default.

* `t.goto(x,y)`
Turtle will jump to the coordinates `(x, y)` without drawing. `x` and `y` should be ints or floats.

* For loops:
```
>for i in range(x):
[tab]>Your code here <---
[tab]>More code in the loop <---
>Code outside of the loop <---
```
>Be sure to indent with a tab for the code you want inside the loop. This will execute the statements inside the loop `x` times with `i` starting at `0` and incrementing to `x-1`. `x` can be a number, but `i` must be a variable.

* `colors=["red","green","purple"]`
Creates a list of colors. You can have more than these three. The statement `colors[0]` accesses the first item of the list, in this case `"red"`. You can use this in conjunction with `t.color(colors[i%3])` to cycle through the colors in the list each time through a loop.

* Arithmetic expressions:
You may use any arithmetic expressions you'd like, such as `x = y/z`.
