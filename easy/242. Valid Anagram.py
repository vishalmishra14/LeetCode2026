"""
242. Valid Anagram
Easy

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sourceHashMap = {}
        targetHashMap  = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            sourceHashMap[s[i]] = sourceHashMap.get(s[i], 0) + 1
            targetHashMap[t[i]] = targetHashMap.get(t[i], 0) + 1

        return sourceHashMap == targetHashMap

solution = Solution()
print(solution.isAnagram("anagram", "nagaram")) # True
print(solution.isAnagram("rat", "car")) # False
print(solution.isAnagram("a", "a")) # True
print(solution.isAnagram("ab", "ba")) # True
print(solution.isAnagram("abc", "cab")) # True
print(solution.isAnagram("abc", "abcd")) # False
print(solution.isAnagram("abcd", "dcba")) # True
print(solution.isAnagram("aabbcc", "abcabc")) # True
print(solution.isAnagram("aabbcc", "aabbc")) # False
print(solution.isAnagram("aabbcc", "aabbcc")) # True
print(solution.isAnagram("abc", "def")) # False
print(solution.isAnagram("abcd", "abdc")) # True
print(solution.isAnagram("abcd", "abcc")) # False
print(solution.isAnagram("a", "b")) # False
print(solution.isAnagram("aa", "aa")) # True
print(solution.isAnagram("aa", "ab")) # False
print(solution.isAnagram("abcde", "edcba")) # True
print(solution.isAnagram("abcde", "abcd")) # False