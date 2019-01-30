

"""
Given a list of integers, return the largest.k

List <- [a, b, c..., z]
1. take a number from the list and 
compare it with another number in the list.
2. Remember the larger number.
3. Repeat until the list is empty: take another number from the
    list and compare the one you remembered and remember the larger one.
4. return the number you remembered
"""

def LargestInt(List):
    result = List[0]
    for n in List:
        if n > result:
            result = n
    return result

x = [-150000000000000000, -50000000000000000]
print(LargestInt(x))







        
