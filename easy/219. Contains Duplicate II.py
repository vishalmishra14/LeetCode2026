"""
219. Contains Duplicate II
Easy

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105

"""
from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ## Method 1 O(n^2)
        # for L in range(len(nums)):
        #     for R in range(L+1, min(len(nums), L+k+1)):
        #         if nums[L] == nums[R]:
        #             return True
        # return False

        ## Method 2 O(n) 
        # using a sliding window of size k and a hashset to check for duplicates in the window

        window = set()
        L = 0

        for R in range(len(nums)):
            if R-L > k:
                window.remove(nums[L])
                L +=1
            if nums[R] in window:
                return True
            window.add(nums[R])

        return False

    
s = Solution()
# print(s.containsNearbyDuplicate([1,2,3,1], 3)) # True
# print(s.containsNearbyDuplicate([1,0,1,1], 1)) # True
# print(s.containsNearbyDuplicate([1,2,3,1,2,3], 2)) # False
print(s.containsNearbyDuplicate([1,2,3,1,2,3],2)) # False