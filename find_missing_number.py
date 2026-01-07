#TODO 1: Write a function find_missing_number(nums) that takes a list of integers from 0 to n with one number missing
# and returns the missing number.


def find_missing_number(nums):
	length_of_nums = len(nums)
	expected_sum_of_nums = length_of_nums * ( length_of_nums + 1 ) // 2
	sum_of_nums = sum(nums)

	missing_num =  expected_sum_of_nums - sum_of_nums

	return missing_num

nums = [3, 0, 1]

print(find_missing_number(nums))