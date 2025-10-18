def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Find two numbers in nums that add up to target.
    
    Args:
        nums: List of integers
        target: Target sum
    
    Returns:
        List of two indices whose corresponding values sum to target
    
    Time Complexity: O(n) - single pass through the array
    Space Complexity: O(n) - hash table to store previously seen numbers
    """
    seen = {}  # num -> index mapping
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            # Return indices in sorted order to match test harness
            return sorted([seen[complement], i])
        seen[num] = i
    return []