
#include <vector>
#include <algorithm>

class Solution {
public:
	double findMedianSortedArrays(const std::vector<int>& nums1, const std::vector<int>& nums2) {
		const std::vector<int>& A = (nums1.size() <= nums2.size()) ? nums1 : nums2;
		const std::vector<int>& B = (nums1.size() > nums2.size()) ? nums1 : nums2;
		int m = A.size(), n = B.size();
		int imin = 0, imax = m, half_len = (m + n + 1) / 2;
		while (imin <= imax) {
			int i = (imin + imax) / 2;
			int j = half_len - i;
			if (i < m && B[j - 1] > A[i]) {
				imin = i + 1;
			} else if (i > 0 && A[i - 1] > B[j]) {
				imax = i - 1;
			} else {
				int max_of_left = 0;
				if (i == 0) { max_of_left = B[j - 1]; }
				else if (j == 0) { max_of_left = A[i - 1]; }
				else { max_of_left = std::max(A[i - 1], B[j - 1]); }
				if ((m + n) % 2 == 1) {
					return max_of_left;
				}
				int min_of_right = 0;
				if (i == m) { min_of_right = B[j]; }
				else if (j == n) { min_of_right = A[i]; }
				else { min_of_right = std::min(A[i], B[j]); }
				return (max_of_left + min_of_right) / 2.0;
			}
		}
		return 0.0; // Should never reach here
	}
};