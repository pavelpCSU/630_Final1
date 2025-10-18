def test_three_sum():
    from solution import three_sum

    # Test case 1: Basic test with positive and negative numbers
    nums1 = [-1, 0, 1, 2, -1, -4]
    expected1 = [[-1, -1, 2], [-1, 0, 1]]
    assert sorted(three_sum(nums1)) == sorted(expected1)

    # Test case 2: No triplets
    nums2 = [1, 2, 3]
    expected2 = []
    assert sorted(three_sum(nums2)) == sorted(expected2)

    # Test case 3: All zeros
    nums3 = [0, 0, 0]
    expected3 = [[0, 0, 0]]
    assert sorted(three_sum(nums3)) == sorted(expected3)

    # Test case 4: Mixed numbers with duplicates
    nums4 = [1, -1, -1, 0]
    expected4 = [[-1, 0, 1]]
    assert sorted(three_sum(nums4)) == sorted(expected4)

    # Test case 5: Large input
    nums5 = [-2, 0, 1, 1, 2]
    expected5 = [[-2, 0, 2], [-1, 0, 1]]
    assert sorted(three_sum(nums5)) == sorted(expected5)

    print("All tests passed!")

if __name__ == "__main__":
    test_three_sum()