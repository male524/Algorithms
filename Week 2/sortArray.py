# 912. Sort an Array
"""
iven an array of integers nums, sort the array in ascending order.

 

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
 

Constraints:

1 <= nums.length <= 50000
-50000 <= nums[i] <= 50000
"""

from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return sorted(nums)

print(Solution.sortArray(1, [5,1,1,2,0,0]))

# I used the built in sorting function to solve this problem
# This took like 1 minute since I kinda cheated
# Write a quick sort and a merge sort