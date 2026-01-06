
# Using the set method
def find_duplicates(nums):
	seen = set()
	duplicates = set()

	for num in nums:
		if num in seen:
			duplicates.add(num)
		seen.add(num)

	return list(duplicates)

print(find_duplicates([1, 2, 3, 4, 2, 1, 2, 5]))