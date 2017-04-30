CS162: Homework 4 - Test Driving a List
======

![Pink Car](car.jpg)

Adapted from David Lu's Winter 2017 CS162 course.

Working with Lists
------

>When you purchase a car, you ought to make a list of the pros and cons of each model under consideration as well as your test driving impressions. For your 4th project, you are to write a program which allows a user to list information about the models of cars they are interested in purchasing. The user may modify listings with notes, including test driving impressions and pros and cons. The program should be able to save and load the list from disk.

### Details
Your list should be implemented as a linear linked list. You may use a `struct` to define a node. All strings must be implemented as dynamically allocated null-terminating arrays. You may not use any global variables. File i/o should be implemented using the `fstream` library.

Each node should have a number of fields corresponding to a car's make, model, year, style (e.g. sedan, coupe, SUV), and price. You may include additional fields if you'd like (horsepower, mileage, etc...). Further, each node should have a list of pros, a list of cons, and a test driving impressions field.

### Program Functionality
The user should be able to...
1. Enter a car with associated information to the list.
1. Save and load their list to the hard drive.
1. Edit a listing to add pros and cons and their driving impressions.
1. Delete a listing from the list.
1. Pretty print the list to the screen.
