#TODO:1 Write a function second_largest(nums) that takes a list of integers and returns the second largest number.

def second_largest(nums):
	if len(nums) < 2:
		return

	largest_num = float("-inf")
	second_largest = float("-inf")

	for num in nums:
		if num > largest_num:
			second_largest = largest_num
			largest_num = num
		elif num < largest_num and num > second_largest:
			second_largest = num

print(second_largest([10, 5, 20, 8]))   # 10
print(second_largest([3, 3, 2, 1]))    # 2
print(second_largest([5]))             # None

