"""
62. Unique Paths
Medium
Topics
premium lock icon
Companies
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
 

Constraints:

1 <= m, n <= 100

"""

class Solution:
    def __init__(self):
        self.r = 0
        self.c = 0
    def uniquePaths(self, m: int, n: int) -> int:
        # # Brute force Methode
        # # recursion solution
        def recursive(r, c):

            if r == m or c == n:
                return 0
            if r == m-1 or c == n-1:
                return 1
            return recursive(r+1, c) + recursive(r, c+1)

        return recursive(0, 0)

        # Memoization approach
        memo = {}
        def recursive_memo(r,c):
            if r == m or c ==n:
                return 0
            if memo[r][c] != -1:
                return memo[r][c]
            if r == m-1 or c == n-1:
                return 1
            memo[r][c] = recursive_memo(r+1, c) + recursive_memo(r, c+1)
            return memo[r][c]

        # Initialize memoization table
        memo = [[-1 for _ in range(n)] for _ in range(m)]
        return recursive_memo(0, 0)

        # Dynamic Programming approach
        preRow = [0] * n
        for i in range(m-1, -1, -1):
            curRow = [0] * n
            curRow[-1] = 1
            for j in range(n-2, -1, -1):
                curRow[j] = curRow[j+1] + preRow[j]
            preRow = curRow
        return preRow[0]



    

# Example usage:
s = Solution()
print(s.uniquePaths(3, 7))  # 28
print(s.uniquePaths(3, 2))  # 3