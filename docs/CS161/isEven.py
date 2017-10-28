def isEven(value):
	numbers = list(range(0, 100))
	odd = False
	for num in numbers:
		if odd:
                    numbers.remove(num)
            #odd = not odd
		if odd:
                    odd = False
                else:
                    odd = True
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


