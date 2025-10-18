#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

// Function to find unique triplets that sum to zero
vector<vector<int>> three_sum(vector<int>& nums) {
    vector<vector<int>> result;
    sort(nums.begin(), nums.end());
    
    for (size_t i = 0; i < nums.size(); ++i) {
        if (i > 0 && nums[i] == nums[i - 1]) continue; // Skip duplicates
        
        size_t left = i + 1;
        size_t right = nums.size() - 1;
        
        while (left < right) {
            int sum = nums[i] + nums[left] + nums[right];
            if (sum == 0) {
                result.push_back({nums[i], nums[left], nums[right]});
                while (left < right && nums[left] == nums[left + 1]) left++; // Skip duplicates
                while (left < right && nums[right] == nums[right - 1]) right--; // Skip duplicates
                left++;
                right--;
            } else if (sum < 0) {
                left++;
            } else {
                right--;
            }
        }
    }
    
    return result;
}

// Test cases for the three_sum function
void run_tests() {
    vector<vector<int>> test_cases = {
        {-1, 0, 1, 2, -1, -4},
        {0, 1, 1},
        {1, 2, -2, -1},
        {},
        {-2, 0, 1, 1, 2}
    };
    
    for (const auto& test : test_cases) {
        vector<vector<int>> result = three_sum(test);
        cout << "Input: ";
        for (int num : test) {
            cout << num << " ";
        }
        cout << "\nOutput: ";
        for (const auto& triplet : result) {
            cout << "[";
            for (int num : triplet) {
                cout << num << " ";
            }
            cout << "] ";
        }
        cout << endl;
    }
}

int main() {
    run_tests();
    return 0;
}