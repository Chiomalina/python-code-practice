# TODO:1 Write a function count_occurrences(words) that takes a list of strings and
#  returns a dictionary with each word as a key and its count as the value.



def count_occurrences(words):
	words_occurrences = {}

	for word in words:
		if word in words_occurrences:
			words_occurrences[word] = words_occurrences.get(word, 0) + 1
		else:
			words_occurrences[word] = 1

	return words_occurrences


list_of_words = ["cat", "dog", "cat"]
print(count_occurrences(list_of_words))




