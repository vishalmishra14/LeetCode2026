from typing import List
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMax = nums[0]
        globalMax = nums[0] # just in case all numbers are negative

        curMin = nums[0]
        globalMin = nums[0] # just in case all numbers are positive
        
        total = nums[0]

        for num in range(1, len(nums)):
            total += nums[num]
            curMax = max(curMax + nums[num], nums[num])
            globalMax = max(globalMax, curMax)

            curMin = min(curMin + nums[num], nums[num])
            globalMin = min(globalMin, curMin)

        if globalMax < 0: # all numbers are negative
            return globalMax
        return max(total-globalMin, globalMax)

# Test cases

s = Solution()
print(s.maxSubarraySumCircular([-2,-3,-1])) # -1