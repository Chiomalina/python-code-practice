#TODO: Write a function find_duplicates(nums) that takes a list of integers and returns a list of all the
# duplicate numbers (each duplicate should appear only once in the result).

# Using the set method
def find_duplicates(nums):
	seen = set()
	duplicate = set()

	for num in nums:
		if num in seen:
			duplicate.add(num)
		seen.add(num)

	return duplicate


print(find_duplicates([1, 2, 3, 4, 2, 1, 2, 5]))