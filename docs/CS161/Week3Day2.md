#CS161 at CCUT Week 3 Day 2: Algorithms

![Fractal Spiral](Fractal.jpg)

Let's take a short break from learning syntax and semantics to step back and think about how to plan and design a program that solves a problem.

Suppose you want to know whether a given positive integer less than 100 is even or odd. What is the process by which you find out?

#### Algorithms
>An algorithm is a sequence of operations that solve a problem or perform a calculation.

Here's an *admittedly poor* algorithm for solving the above problem, written in Python-like pseudo code:

```py
def isEven(value):
  let numbers be a list of numbers from 0 to 99
  let odd = False
  for x in numbers:
    if odd:
      remove x from numbers
    odd = not odd
  if value in numbers:
    return True
  else:
    return False
```

>Pseudo code is an informal high level description of an algorithm. It uses many of the conventions of a programming language but is intended for human readability. There is no official way to write pseudo code, but I like Python-style pseudo code. It's easy to read and write and it's easy to turn into Python when you're ready. However, it's up to you to find a balance between detail and high level concepts.

Here's the function in Python:
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

Here's a line by line explanation. The first line let us know we have one input `value`, the given number to be checked. The next line says create a list of numbers from `0` to `99` and call it `numbers`. The third says to keep track of a variable called `odd`, which we initialize to `False`. Then we check each number in `numbers`. If `odd` is `True` at the time, then we remove that number from the list. Then we flip `odd`s boolean value. After processing the entire list this way, removing every other number, we check to see whether `value` is in the list. If so, then return `True`, else return `False`.

Two questions:
* Does this solve the problem we initially wanted to solve?
* Is it an efficient procedure?

To test this function, we need some additional code:

```py
num = int(input("Give me a number from 0 to 99"))
if isEven(num):
  print("This number is even")
else:
  print("This number is odd")
```

Try it out. Does it work as we expected?

Can you think of a better algorithm to solve this problem?

Before you begin writing code to tackle a problem, you should first think about what sequence of operations need to be done in order to solve the problem. You should probably write it out in pseudo code so that you can look at it and think about whether it will work or not.

Let's try to design a better version of this function together.

#### Additional Exercises
* Design an algorithm that returns the largest integer within a list of integers.

* Design an algorithm that returns true if a name is found within a list of names and false otherwise.

  * Suppose the list is *sorted* alphabetically.

* Design an algorithm that takes a lists of numbers and returns a list of numbers sorted from smallest to largest.

<!---
--------
#C++

In CS162, CS163, and CS202, you will learn C++. You might wonder why you learn C++ if Python is so much quicker to get started with.


#### Comments

#### Variables


##### Identifiers
##### Declaration and initialization
##### Assignment with `=`


#### Input/Output with iostream library

#### Arithmetical operators

#### Loops

##### For loop

##### While loop

##### Do... while loop


#### Functions

--->
