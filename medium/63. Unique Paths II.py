"""

63. Unique Paths II
Medium


You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
Example 2:


Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
 

Constraints:

m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] is 0 or 1.


"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        ##Bottom up approach: True Dynamic programming
        r, c = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * c
        dp[c-1] = 1

        for i in range(r-1, -1, -1):
            for j in range(c-1, -1, -1):
                if obstacleGrid[i][j]:
                    dp[j] = 0
                elif j + 1 < c:
                    dp[j] = dp[j] + dp[j+1]
        return dp[0]

    
        ## Memoization 

        memo = {}
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])

        def dfs(r, c):
            if min(r,c) < 0  or r == ROWS or c == COLS or obstacleGrid[r][c] == 1:
                return 0
            if (r, c) in memo:
                return memo[(r,c)]
            if r == ROWS - 1 and c == COLS - 1:
                return 1
            memo[(r,c)] = dfs(r+1,c) + dfs(r, c+1)
            return memo[(r,c)]

        return dfs(0,0)
        ### DFS backtracking

        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        visit = set()

        def recursive(r, c):
            if min(r,c) < 0 or r == ROWS or c == COLS or (r,c) in visit or \
               obstacleGrid[r][c] == 1:
                return 0
            if r == ROWS - 1 and c == COLS -1:
                return 1
            visit.add((r,c))
            count = 0
            count += recursive(r+1, c)
            count += recursive(r, c+1)
            visit.remove(((r,c)))
            return count
        return recursive(0,0)
solution = Solution()
print(solution.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])) # 2
print(solution.uniquePathsWithObstacles([[0,1],[0,0]])) # 1
print(solution.uniquePathsWithObstacles([[1,0],[0,0]])) # 0
print(solution.uniquePathsWithObstacles([[0,0],[1,1],[0,0]])) # 0
print(solution.uniquePathsWithObstacles([[0]])) # 1
print(solution.uniquePathsWithObstacles([[1]])) # 0
print(solution.uniquePathsWithObstacles([[0,0,0],[0,0,0],[0,0,0]])) # 6
print(solution.uniquePathsWithObstacles([[0,0],[0,1]])) # 0
print(solution.uniquePathsWithObstacles([[0,0,0],[0,0,0],[0,1,0]])) # 3

