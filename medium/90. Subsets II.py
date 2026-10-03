"""
90. Subsets II
Medium

Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
"""

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset[:])
                return

            # To include the number 
            subset.append(nums[i])
            dfs(i+1)

            # Not to include the number
            subset.pop()
            # Skip duplicates
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i+1)

        dfs(0)
        return res

sol = Solution()
print(sol.subsetsWithDup([1,2,2]))
print(sol.subsetsWithDup([0]))
print(sol.subsetsWithDup([1,2]))
print(sol.subsetsWithDup([1]))
print(sol.subsetsWithDup([]))