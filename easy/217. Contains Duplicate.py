"""
217. Contains Duplicate
Easy
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109

"""
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for num in nums:
            count[num] = count.get(num,0) + 1
            if count[num] > 1:
                return True
        return False
        # L = 0

        # for R in range(1,len(nums)):
        #     if nums[R] == nums[L]:
        #         return True
        #     L +=1
        # return False
s = Solution()
print(s.containsDuplicate([1,2,3,1])) # True
print(s.containsDuplicate([1,2,3,4])) # False
