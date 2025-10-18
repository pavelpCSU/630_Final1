def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    """
    Find the median of two sorted arrays with O(log(m+n)) complexity.
    
    Args:
        nums1: First sorted array
        nums2: Second sorted array
        
    Returns:
        float: Median of the two arrays
    """
    # Ensure nums1 is the smaller array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)
    total = m + n
    half = (total + 1) // 2
    
    left, right = 0, m
    
    while left <= right:
        # Try a partition point in nums1
        partitionX = (left + right) // 2
        # Calculate corresponding partition point in nums2
        partitionY = half - partitionX
        
        # Get values around partition points
        maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
        minRightX = float('inf') if partitionX == m else nums1[partitionX]
        
        maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
        minRightY = float('inf') if partitionY == n else nums2[partitionY]
        
        # Check if we found the right partition
        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            # If total length is odd
            if total % 2 == 1:
                return max(maxLeftX, maxLeftY)
            # If total length is even
            return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
            
        # Adjust the partition
        elif maxLeftX > minRightY:
            right = partitionX - 1
        else:
            left = partitionX + 1
            
    # Should never reach here if input arrays are sorted
    return 0.0
