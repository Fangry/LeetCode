#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = {}
        window_start = 0
        result = 0
        for window_end in range(len(s)):
            if s[window_end] in m:
                window_start = max(window_start, m[s[window_end]])
            result = max(result, window_end - window_start + 1)
            m[s[window_end]] = window_end + 1
        return result
                    


        
# @lc code=end
