def isEven(value):
    numbers = list(range(0, 100))
    print(numbers)
    odd = False
    for num in range(0, 100):
    #for num in numbers:
        if odd:
            numbers.remove(num)
        odd = not odd
        #print(odd, num, numbers)
    print(numbers)
    if value in numbers:
        return True
    else:
        return False

num = int(input("Give me a number"))
if isEven(num):
    print("This number is even")
else:
    print("This number is odd")
