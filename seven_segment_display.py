DIGITS = [
    ["###", "# #", "# #", "# #", "###"],  # 0
    ["  #", "  #", "  #", "  #", "  #"],  # 1
    ["###", "  #", "###", "#  ", "###"],  # 2
    ["###", "  #", "###", "  #", "###"],  # 3
    ["# #", "# #", "###", "  #", "  #"],  # 4
    ["###", "#  ", "###", "  #", "###"],  # 5
    ["###", "#  ", "###", "# #", "###"],  # 6
    ["###", "  #", "  #", "  #", "  #"],  # 7
    ["###", "# #", "###", "# #", "###"],  # 8
    ["###", "# #", "###", "  #", "###"],  # 9
]

number = str(input("Enter a number: "))

if number == "":
	print("")

elif not number.isdigit():
	print("ValueError: number must be a non-negative integer. (digits only)")
else:
	for row in range(5):
		line_parts = []
		for char in number:
			digit = int(char)
			line_parts.append(DIGITS[digit][row])
			print("".join(line_parts))
