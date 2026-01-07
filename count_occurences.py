# TODO:1 Write a function find_duplicates(nums) that takes a list of integers and returns a list of all the duplicate
#  numbers (each duplicate should appear only once in the result).

def count_occurrences(sub):
	result = {}

	for word in words:
		if word in result:
			result[word] = result[word] + 1
		else:
			result[word] = 1

	return result

def count_occurrences_alt(sub):
	count ={}

	for word in words:
		count[word] = count.get(word, 0) + 1

	return count

words = ["cat", "dog", "cat"]
print(count_occurrences(words))
print("Alternative solution: ", count_occurrences_alt(words))