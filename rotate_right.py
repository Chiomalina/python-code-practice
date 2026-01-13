
def rotate_num_to_right(nums, k):
	if len(nums) < 0: return

	new_k = k % len(nums)

	returned_value = nums[new_k:] + nums[:new_k]

	return returned_value


list_of_nums = [1, 2, 3, 4, 5]
rotation_value = 2

print(rotate_num_to_right(list_of_nums, rotation_value))


