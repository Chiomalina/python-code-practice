#TODO: Write a function find_duplicates(nums) that takes a list of integers and returns a list of all the
# duplicate numbers (each duplicate should appear only once in the result).

# Using the set method
def find_duplicates_1(nums):
	seen = set()
	duplicates = set()

	for num in nums:
		if num in seen:
			duplicates.add(num)
		seen.add(num)

	return list(duplicates)


def find_duplicates_2(nums):
	seen = {}
	duplicate = []

	for num in nums:
		if num in seen:
			if seen[num] == 1:
				duplicate.append(num)
			seen[num] += 1

		else:
			seen[num] = 1

	return duplicate



list_of_nums = [1, 2, 3, 4, 2, 1, 2, 5]

print(find_duplicates_1(list_of_nums))
print(find_duplicates_2(list_of_nums))