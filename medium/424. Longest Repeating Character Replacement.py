"""
424. Longest Repeating Character Replacement
Medium

You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

Example 1:

Input: s = "XYYX", k = 2

Output: 4
Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

Example 2:

Input: s = "AAABABB", k = 1

Output: 5
Constraints:

1 <= s.length <= 1000
0 <= k <= s.length

"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ## Method 1
        # count = [0] * 26
        # max_count = 0
        # left = 0
        # result = 0

        # for right in range(len(s)):
        #     count[ord(s[right]) - ord('A')] += 1
        #     max_count = max(max_count, count[ord(s[right]) - ord('A')])

        #     while right - left + 1 - max_count > k:
        #         count[ord(s[left]) - ord('A')] -= 1
        #         left += 1

        #     result = max(result, right - left + 1)
        
        ## Method 2
        result = 0
        count, L = {}, 0
        for R in range(len(s)):
            count[s[R]] = count.get(s[R], 0) + 1
            while R-L+1-max(count.values())>k:
                count[s[L]] -= 1
                L += 1
            result = max(result, R-L+1)
        return result   
    
s = Solution()
print(s.characterReplacement("ABAB", 2)) # 4
print(s.characterReplacement("AAABABB", 1)) # 5
