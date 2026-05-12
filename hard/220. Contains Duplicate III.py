"""
220. Contains Duplicate III
Hard
You are given an integer array nums and two integers indexDiff and valueDiff.

Find a pair of indices (i, j) such that:

i != j,
abs(i - j) <= indexDiff.
abs(nums[i] - nums[j]) <= valueDiff, and
Return true if such pair exists or false otherwise.

 

Example 1:

Input: nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
Output: true
Explanation: We can choose (i, j) = (0, 3).
We satisfy the three conditions:
i != j --> 0 != 3
abs(i - j) <= indexDiff --> abs(0 - 3) <= 3
abs(nums[i] - nums[j]) <= valueDiff --> abs(1 - 1) <= 0
Example 2:

Input: nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
Output: false
Explanation: After trying all the possible pairs (i, j), we cannot satisfy the three conditions, so we return false.
 

Constraints:

2 <= nums.length <= 105
-109 <= nums[i] <= 109
1 <= indexDiff <= nums.length
0 <= valueDiff <= 109

"""
from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        window = set()

        L = 0

        for R in range(len(nums)):
          if R-L > indexDiff:
            window.remove(nums[L])
            L +=1
          if nums[R] in window:
             if abs(nums[R] - nums[L]) <= valueDiff:
                return True
          window.add(nums[R])
        return False
    
s = Solution()
# print(s.containsNearbyAlmostDuplicate([1,2,3,1], 3, 0)) # True
# print(s.containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 3)) # False

print(s.containsNearbyAlmostDuplicate([8,7,15,1,6,1,9,15], 1, 3)) # True
        