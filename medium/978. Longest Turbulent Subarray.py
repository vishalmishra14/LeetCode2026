"""
978. Longest Turbulent Subarray
Medium
Topics
premium lock icon
Companies
Given an integer array arr, return the length of a maximum size turbulent subarray of arr.

A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:

For i <= k < j:
arr[k] > arr[k + 1] when k is odd, and
arr[k] < arr[k + 1] when k is even.
Or, for i <= k < j:
arr[k] > arr[k + 1] when k is even, and
arr[k] < arr[k + 1] when k is odd.
 

Example 1:

Input: arr = [9,4,2,10,7,8,8,1,9]
Output: 5
Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]
Example 2:

Input: arr = [4,8,12,16]
Output: 2
Example 3:

Input: arr = [100]
Output: 1
 

Constraints:

1 <= arr.length <= 4 * 104
0 <= arr[i] <= 109


"""
from typing import List
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        L, R, prev, max_len = 0, 1, "", 1

        # if len(arr) == 1:
        #     return 1

        # for R in range(1, len(arr)):
        #     if arr[R] == arr[R-1]:
        #         L = R
        #     elif R == len(arr)-1 or (arr[R] > arr[R+1] and arr[R-1] < arr[R]) or (arr[R] < arr[R+1] and arr[R-1] > arr[R]):
        #         if R == len(arr)-1:
        #             max_len = max(max_len, R-L)
        #         else:
        #             max_len = max(max_len, R-L+1)
        #     else:
        #         L = R-1
        # return max_len
    
    
        if len(arr) == 1:
            return 1
        while R < len(arr):
            if arr[R] > arr[R-1] and prev != ">":
                max_len = max(max_len, R-L+1)
                prev = ">"
                R += 1
            elif arr[R] < arr[R-1] and prev != "<":
                max_len = max(max_len, R-L+1)
                prev = "<"
                R += 1
            else:
                R = R+1 if arr[R] == arr[R-1] else R
                L = R-1
                prev = ""
        return max_len
s = Solution()
print(s.maxTurbulenceSize([9,4,2,10,7,8,8,1,9])) # 5
print(s.maxTurbulenceSize([4,8,12,16])) # 2 

