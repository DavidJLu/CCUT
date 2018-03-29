def isEven(value):
    if value % 2 == 0:
        return True
    else:
        return False

num = int(input("Give me a number"))
if isEven(num):
    print("This number is even")
else:
    print("This number is odd")
