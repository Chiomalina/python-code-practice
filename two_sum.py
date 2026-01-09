#TODO: Write a function two_sum(nums, target) that takes a list of integers nums and an integer target.
# Return a list of two indices whose values add up to the target. Assume there is exactly one solution.

def two_sum(nums, target):

	seen = {}

	for index, num in enumerate(nums):
		complement = target - num

		if complement in seen:
			return [seen[complement], index]
		else:
			seen[num] = index





nums_1 = [2, 7, 11, 15]
nums_2 = [2, 5, 10, 8, 5, 4]
target = 9

print(two_sum(nums_1, target))
print(two_sum(nums_2, target))