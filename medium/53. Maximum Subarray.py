## Kadane's Algorithm
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Method 1 BruteFore O(n^2)
        maxSum = float('-inf')
        curSum = 0
        # if len(nums) == 1:
        #     return nums[0]
        # for i in nums:
        #     for j in nums:
        #         curSum = i + j
        #         if curSum > maxSum:
        #             maxSum = curSum

        ## Method2 O(n)
        for n in nums:
            curSum = max(curSum, 0)
            curSum +=n
            maxSum = max(maxSum, curSum)

        return maxSum