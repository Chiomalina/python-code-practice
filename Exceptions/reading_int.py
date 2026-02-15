import sys


def read_int(prompt, min, max):
	#
	# Write your code here.
	#
	while True:

		try:
			user_input = int(input(prompt))
			if user_input < -10 or user_input > 10:
				print("Error: the value is not within permitter range (min..max")
				print("Input the value again")
		except ValueError:
			print("Error: wrong input")
			user_input
		else:
			print(user_input)
			sys.exit(1)


v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
