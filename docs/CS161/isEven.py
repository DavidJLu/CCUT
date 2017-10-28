def isEven(value):
    numbers = list(range(0, 100))
    print(numbers)
    odd = True
    for num in range(0, 100):
        odd = not odd
        print(num, odd)
        if odd:
            numbers.remove(num)
        #odd = not odd
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
