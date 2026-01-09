import math

def factorial(number):
	if number < 0: return

	if number == 0 or number == 1: return 1
	return number * factorial(number -1)

print(factorial(4))

print(math.factorial(4))