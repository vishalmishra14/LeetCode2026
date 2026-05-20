"""
42. Trapping Rain Water
Hard
Topics
premium lock icon
Companies
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105


"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        L, R, max_left, max_right, final_trapped = 0, len(height) - 1, height[0], height[-1], 0

        while L <= R:
            if max_left <= max_right:
                max_left = max(max_left, height[L])
                final_trapped += (max_left - height[L])
                L += 1

            else:
                max_right = max(max_right, height[R])
                final_trapped += (max_right - height[R])
                R -= 1
        return final_trapped
        # L, R = 0, 1
        # final_trapped = 0
        # local_trapped = 0

        # while R < len(height):
        
        #     if height[R] >= height[L]:
        #         final_trapped += local_trapped
        #         L = R
        #         local_trapped = 0
        #     else:
        #         local_trapped += (height[L] - height[R])
        #     R += 1
        # return final_trapped

s = Solution()
print(s.trap([0,2,0,3,1,0,1,3,2,1])) # 9
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
print(s.trap([4,2,0,3,2,5])) # 9