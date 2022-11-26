from typing import List
#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        lst = []

        def dfs(curr, idx, target):
            if target == 0:
                lst.append(curr.copy())
            if target < 0:
                return
            
            prev = -1
            for i in range(idx, len(candidates)):
                if prev != candidates[i]:
                    curr.append(candidates[i])
                    dfs(curr, i+1, target-candidates[i])
                    curr.pop()
                    prev = candidates[i]
        
        dfs([], 0, target)
        return lst


# @lc code=end

