def three_sum(nums):
    nums.sort()
    triplets = []
    n = len(nums)

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                triplets.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return triplets

# Test cases
def run_tests():
    test_cases = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
        ([], []),
        ([1, 2, -2, -1], [])
    ]

    for i, (nums, expected) in enumerate(test_cases):
        result = three_sum(nums)
        assert sorted(result) == sorted(expected), f"Test case {i + 1} failed: expected {expected}, got {result}"

if __name__ == "__main__":
    run_tests()