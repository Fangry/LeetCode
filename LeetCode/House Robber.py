from typing import List
#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def dfs(i, steal):
            if i >= len(nums):
                return 0
            elif (i, steal) in dp:
                return dp[(i, steal)]
            dp[(i, steal)] = max(dfs(i + 2, True) + nums[i], dfs(i + 1, False))
            return dp[(i, steal)]
        result = dfs(0, True)
        return result

# @lc code=end
solution = Solution()
print(solution.rob([1, 2, 3, 1]))
