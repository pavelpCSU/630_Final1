#ifndef SOLUTION_HPP
#define SOLUTION_HPP

#include <vector>
#include <algorithm>
#include <climits>

class Solution {
public:
    double findMedianSortedArrays(const std::vector<int>& nums1, const std::vector<int>& nums2) {
        // Ensure nums1 is the smaller array for simpler implementation
        if (nums1.size() > nums2.size()) {
            return findMedianSortedArrays(nums2, nums1);
        }
        
        const int m = nums1.size();
        const int n = nums2.size();
        const int total = m + n;
        
        int left = 0, right = m;
        
        while (left <= right) {
            const int partitionX = (left + right) / 2;
            const int partitionY = (total + 1) / 2 - partitionX;
            
            // Get the four boundary elements
            const int maxLeftX = (partitionX == 0) ? INT_MIN : nums1[partitionX - 1];
            const int minRightX = (partitionX == m) ? INT_MAX : nums1[partitionX];
            const int maxLeftY = (partitionY == 0) ? INT_MIN : nums2[partitionY - 1];
            const int minRightY = (partitionY == n) ? INT_MAX : nums2[partitionY];
            
            // Check if we found the right partition
            if (maxLeftX <= minRightY && maxLeftY <= minRightX) {
                // If total length is odd
                if (total % 2 == 1) {
                    return std::max(maxLeftX, maxLeftY);
                }
                // If total length is even
                return (std::max(maxLeftX, maxLeftY) + std::min(minRightX, minRightY)) / 2.0;
            }
            // Adjust the partition
            else if (maxLeftX > minRightY) {
                right = partitionX - 1;
            }
            else {
                left = partitionX + 1;
            }
        }
        
        // We should never reach here if input arrays are sorted
        return 0.0;
    }
};

#endif // SOLUTION_HPP