CS161: Homework 7 - Letter Matrix
======

```
     ___           _______.  ______  __   __          ___      .______     .___________.
    /   \         /       | /      ||  | |  |        /   \     |   _  \    |           |
   /  ^  \       |   (----`|  ,----'|  | |  |       /  ^  \    |  |_)  |   `---|  |----`
  /  /_\  \       \   \    |  |     |  | |  |      /  /_\  \   |      /        |  |     
 /  _____  \  .----)   |   |  `----.|  | |  |     /  _____  \  |  |\  \----.   |  |     
/__/     \__\ |_______/     \______||__| |__|    /__/     \__\ | _| `._____|   |__|    
```

ASCII ART
--------
>Summary: Create a two-dimensional character array, into which you place a pattern. This array is copied with modifications into another array, and both are printed.

#### Detailed Specification:
Create the two-dimensional array of characters, named `a[][]`. There must be at least 20 columns and 30 rows. Initialize `a[][]` as follows: Fill all positions with the ASCII character ‘.’. Then place the ASCII character ‘a’ into all rows and columns, except for the first and last rows and columns, such that a capital letter A is formed. Print this array `a[][]`. Then assign `a[][]` to another matrix `b[][]` but with the following modifications: All 4 corner positions of `b[][]` will hold the character ‘+’. All other topmost and bottommost row positions hold the ‘-‘ character. All other leftmost and rightmost positions hold ‘|’. All positions in `a[][]` that hold an ‘a’ will be assigned an ‘A’ in `b[][]`. And all positions in `a[][]` that hold a ‘.’ will be assigned the blank character ‘ ‘ in `b[][]`. Print `b[][]`. Finally, print `b[][]` in reversed order of rows, so that an upside down ‘A’ will result.
