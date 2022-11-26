from typing import List
#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        lst = []

        def backtracking(x, cur):
            if len(cur) == k:
                lst.append(cur.copy())
            for i in range(x + 1, n + 1):
                backtracking(i, cur + [i])
            
        backtracking(0, [])
        return lst

        
# @lc code=end

