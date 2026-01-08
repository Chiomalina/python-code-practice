#TODO 1: Write a function find_missing_number(nums) that takes a list of integers from 0 to n with one number missing
# and returns the missing number.


def find_missing_number(nums):
	length_of_numbers = len(nums)
	expected_sum_of_numbers = length_of_numbers * (length_of_numbers + 1) // 2
	actual_sum_of_numbers = sum(nums)

	missing_number = expected_sum_of_numbers - actual_sum_of_numbers

	return missing_number

list_of_nums = [0, 1, 3]

print(find_missing_number(list_of_nums))