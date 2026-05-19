"""
11. Container With Most Water
Medium

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
 


"""
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        L, R = 0, len(height)-1
        max_area = 0
        cur_area = 0
        while L < R:
            cur_area = (R - L) * min(height[L], height[R])
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
            max_area = max(max_area, cur_area)
        return max_area        
        # L, max_area, cur_area = 0, 0, 0

        # for R in range(1, len(height)):
            
        #     if height[R] > height[L]:
        #         L = R
        #     else:
        #         cur_area = height[R] * (R - L)
        #     max_area = max(max_area, cur_area)
        # return max_area
    
s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7])) # 49
print(s.maxArea([1,1])) # 1
print(s.maxArea([1,7,2,5,4,7,3,6])) # 36
print(s.maxArea([1,7,2,5,12,3,500,500,7,8,4,7,3,6])) # 500
print(s.maxArea([1,2,1])) # 2

                
