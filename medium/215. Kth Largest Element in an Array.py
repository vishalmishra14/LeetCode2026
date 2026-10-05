"""
215. Kth Largest Element in an Array
Solved
Medium

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104

"""

from typing import List
import random


class Solution:

    # Method 1
    def partition(self, nums: List[int], left: int, right: int):
        pivot = nums[right]
        i = left
        for j in range(left,right):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i +=1
        nums[i], nums[right] = nums[right], nums[i]
        return i

    def findKthLargest(self, nums: List[int], k: int) -> int:
 
        left, right = 0, len(nums)-1

        while left <= right:
            random_pivot_index = random.randint(left, right)
            nums[right], nums[random_pivot_index] = nums[random_pivot_index], nums[right]

            pivot = self.partition(nums, left, right)

            if pivot == len(nums)-k:
                return nums[pivot]
            elif pivot < len(nums)-k:
                left = pivot + 1
            else: 
                right = pivot - 1


    # Method 2: Using heapq (min-heap)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        return heapq.nlargest(k, nums)[-1]

    ## Method 3: using heapq
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        if len(nums) == 1:
            return nums[0]
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]


solution = Solution()
print(solution.findKthLargest([3,2,1,5,6,4], 2)) # 5
print(solution.findKthLargest([3,2,3,1,2,4,5,5,6], 4)) # 4
print(solution.findKthLargest([1,2,3,4,5,6,7,8,9,10], 1)) # 10
print(solution.findKthLargest([1,2,3,4,5,6,7,8,9,10], 10)) # 1
print(solution.findKthLargest([10,9,8,7,6,5,4,3,2,1], 5)) # 6