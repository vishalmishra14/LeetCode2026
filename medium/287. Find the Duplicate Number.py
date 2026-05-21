"""
287. Find the Duplicate Number
Medium

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [3,3,3,3,3]
Output: 3
 

Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.
 

Follow up:

How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?

"""
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Method 1 Floyd's Tortoise and Hare (Cycle Detection)
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2= 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
            
        # # Method 2 
        # for i in range(len(nums)):
        #     if i < len(nums) and nums[i] in nums[i+1:]:
        #         return nums[i]
            
s = Solution()
print(s.findDuplicate([1,3,4,2,2])) # 2
print(s.findDuplicate([3,1,3,4,2])) # 3
print(s.findDuplicate([3,3,3,3,3])) # 3
        