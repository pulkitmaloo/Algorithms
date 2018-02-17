def missing_posnum(arr):
	"""
	Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
	"""
	arr_dict = {x:True for x in arr}
	for i in range(1, len(arr)+1):
		if i not in arr_dict:
			return i
	return False	# No solution


if __name__ == "__main__":
	arr = [1, 2, 0]
	res = missing_posnum(arr)
	print(res)
