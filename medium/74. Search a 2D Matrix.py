"""
74. Search a 2D Matrix
Medium
Topics
premium lock icon
Companies
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:



Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104

"""
from typing import List

class Solution:
    def binarySearch(self, arr: List[int], target: int) -> bool:
        L, R = 0 , len(arr) - 1
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Brute Force TC O(m * n)
        # for num in matrix:
        #     if target in num:
        #         return True
        # return False

        # # Staircase Search  TC O(m + n)
        # row, cols = 0, len(matrix[0]) - 1
        # while row < len(matrix) and cols >= 0:
        #     if matrix[row][cols] > target:
        #         cols -= 1
        #     elif matrix[row][cols] < target:
        #         row += 1
        #     else:
        #         return True
        # return False
    
        # Binary Search
        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, ROWS * COLS - 1
        while l <= r:
            mid = l + (r - l) // 2

            row, col = mid // COLS, mid % COLS
            if matrix[row][col] > target:
                r = mid - 1
            elif matrix[row][col] < target:
                l = mid + 1
            else:
                return True
        return False

        
s = Solution()
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)) #True
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)) #False