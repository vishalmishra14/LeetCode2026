"""
3. Longest Substring Without Repeating Characters

Medium
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.


"""



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        length = 0
        window = set()

        for R in range(len(s)):
            while s[R] in window:
                window.remove(s[L])
                L +=1
            window.add(s[R])
            length = max(length, R-L+1)
        return length  
s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb")) # 3
print(s.lengthOfLongestSubstring("bbbbb")) # 1
print(s.lengthOfLongestSubstring("pwwkew")) # 3
print(s.lengthOfLongestSubstring("")) # 0
print(s.lengthOfLongestSubstring(" ")) # 1