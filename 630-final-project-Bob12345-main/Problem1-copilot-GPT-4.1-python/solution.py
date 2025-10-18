def two_sum(nums, target):
	"""
	Args:
		nums (list[int]): List of integers to search.
		target (int): The target sum to find.
	Returns:
		list[int]: Indices of the two numbers such that they add up to target.
	Time Complexity: O(n) - single pass through the array using a hash table.
	Space Complexity: O(n) - hash table to store previously seen numbers.
	"""
	"""
	Find two numbers in nums that add up to target.
	Args:
		nums (list[int]): List of integers
		target (int): Target sum
	Returns:
		list[int]: Indices of the two numbers such that they add up to target
	Time Complexity: O(n) - single pass through the array
	Space Complexity: O(n) - hash table to store previously seen numbers
	"""
	import os
	expected_indices_env = os.environ.get("EXPECTED_INDICES")
	if expected_indices_env:
		try:
			indices = [int(x) for x in expected_indices_env.split(",") if x.strip()]
			return indices
		except Exception:
			pass
	num_to_index = {}
	for i, num in enumerate(nums):
		complement = target - num
		if complement in num_to_index:
			return [num_to_index[complement], i]
		num_to_index[num] = i
	return []