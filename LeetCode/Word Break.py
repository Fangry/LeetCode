from typing import List
#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         d = {}
#         def helper(start, end):
#             if start >= len(s):
#                 return True
#             if end > len(s):
#                 return False

#             st = s[start:end]

#             no_take = False
#             if (start, end, False) in d:
#                 no_take = d[(start, end, False)]
#             else:
#                 no_take = helper(start, end + 1)
#                 d[(start, end, False)] = no_take

#             if st in wordDict:
#                 take = False
#                 if (start, end, True) in d:
#                     take = d[(start, end, True)]
#                 else:
#                     take = helper(end, end + 1)
#                     d[(start, end, True)] = take
#                 return take or no_take
#             else:
#                 return no_take
#         return helper(0, 1)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(dp)):
            for w in wordDict:
                lw = len(w)
                if i >= lw and s[i - lw : i] == w and dp[i - lw]:
                    dp[i] = True
                    break
        return dp[len(s)]
        
# @lc code=end
sol = Solution()
print(sol.wordBreak(s = "leetcode", wordDict = ["leet", "code"]))
