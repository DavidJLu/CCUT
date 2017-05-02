CS163: Homework 3 - Binary Search Tree

![Lone Tree](bst.jpg)

Course Listing
=====

> For this assignment, you are to create a program that holds a searchable list of courses. The goal is to practice implementing a binary search tree with functionality like insert, search, remove by match, remove all, display in sorted order, and so on recursively.

Details
-------
Your binary search tree should be implemented as a class with at least the following methods:

1. Constructor (you are allowed to load from an external file or not)
2. Destructor (call a recursive function to deallocate the tree)
3. Insert course information(add the course information into the tree)
4. Retrieveby number (retrieve all courses based on the course number)
5. Retrieve a range (retrieve all courses within a range of course numbers)
6. Display all
7. Remove (remove by course number)
8. Remove all (remove everything)

Each node of the tree should contain pointers to the left and right children as well as course information. A course has the following fields:

* Course number (e.g., CS163)
* Course name (e.g., Data Structures)
* Section Number (e.g. 001)
* CRN (Course Resource Number)
* Day and Time of the class (e.g., T/TH 10-11:50)
* Course Description

### Requirements:
1) Do  not  use  statically  allocated  arrays  in  your  classes  or  structures.  All memory must be dynamically allocated and kept to a minimum.
2) All data members in a class must be private.
3) Never perform input operations from your class in CS163.
4) Global variables are not allowed in CS163
5) Do not use the String class. (Use arrays of characters instead and the cstring library.)
6) Use modular design, separating the .h files from the .cpp files. Remember, .h files should contain the class header and any necessary prototypes. The .cpp files should contain function definitions. You must have at least 1 .h file and 2 .cpp files. Never "#include" .cpp files.
7) Use the iostream library for all I/O; do not use stdio.h.
8) Make  sure  to  define  a  constructor  and  destructor  for  your  class.  Your destructor
must deallocate all dynamically allocated memory.
