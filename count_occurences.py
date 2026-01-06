# Count occurrences

def count_occurrences(words):
	result = {}

	for word in words:
		if word in result:
			result[word] = result[word] + 1
		else:
			result[word] = 1

	return result

words = ["cat", "dog", "cat"]
print(count_occurrences(words))