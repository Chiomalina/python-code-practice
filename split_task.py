def mysplit(strng):
	result = []
	word = ""

	for char in strng:
		if char.isspace():
			if word:
				result.append(word)
				word = ""
		else:
			word += char

	return result





print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))