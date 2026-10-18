"""
1143. Longest Common Subsequence
Medium
Topics
premium lock icon
Companies
Hint
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.

"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ## Bottom up approach:
        r, c = len(text1), len(text2) + 1
        preRow = [0] * c
        for i in range(r-1,-1,-1):
            curRow = [0] * c
            for j in range(c-2, -1, -1):
                if text1[i] == text2[j]:
                    curRow[j] = 1 + preRow[j+1]
                else:
                    curRow[j] = max(curRow[j+1], preRow[j])
            preRow = curRow
        return preRow[0]
        
        # ## Memoization:
        # memo = {}

        # def dfs(i1, i2):
        #     if i1 == len(text1) or i2 == len(text2):
        #         return 0
        #     if (i1, i2) in memo:
        #         return memo[(i1, i2)]
        #     if text1[i1] == text2[i2]:
        #         memo[(i1, i2)] =  1 + dfs(i1 + 1, i2 + 1)
        #     else:
        #         memo[(i1, i2)] = max(dfs(i1+1, i2), dfs(i1, i2 + 1))
        #     return memo[(i1, i2)]

        # return dfs(0, 0)


        # ## DFS backtracking: Recursive solution

        # def dfs(i1, i2):
        #     if i1 == len(text1) or i2 == len(text2):
        #         return 0
        #     if text1[i1] == text2[i2]:
        #         return 1 + dfs(i1 + 1, i2 + 1)
        #     else:
        #         return max(dfs(i1+1, i2), dfs(i1, i2 + 1))

        # return dfs(0,0)

s = Solution()
print(s.longestCommonSubsequence("abcde", "ace")) # 3
print(s.longestCommonSubsequence("abc", "abc")) # 3
print(s.longestCommonSubsequence("abc", "def")) # 0
print(s.longestCommonSubsequence("abcba", "abcbcba")) # 5

        