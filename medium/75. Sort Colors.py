"""
75. Sort Colors
Medium

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
 

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
 

Follow up: Could you come up with a one-pass algorithm using only constant extra space?



"""
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # # This is 2 pass solution
        # # counts = [0] * len(set(nums))
        # counts = {}

        # for num in nums:
        #     counts[num] = counts.get(num, 0) + 1
        
        # index = 0
        # for n in set(nums):
        #     for _ in range(counts[n]):
        #         nums[index] = n
        #         index += 1
        # return nums
    
        # The one pass solution is to use 3 pointers, one for each color. We can keep track of the current position of each color and swap the elements accordingly. This way we can sort the array in one pass and with constant extra space.
        L, R = 0, len(nums) - 1
        i  = 0 

        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        while i <= R:
            if nums[i] == 0:
                swap(i, L)
                L +=1
            elif nums[i] == 2:
                swap(i, R)
                R -=1
                i -=1
            i +=1
        return nums


s = Solution()
print(s.sortColors([2,0,2,1,1,0])) # [0,0,1,1,2,2]
print(s.sortColors([2,0,1])) # [0,1,2]
print(s.sortColors([3, 3, 1, 1, 0, 0, 3])) # [0,0,1,1,3,3,3]