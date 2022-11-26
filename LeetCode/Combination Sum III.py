from typing import List
#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        lst = []

        def backtracking(cur, i, cur_sum):
            if cur_sum == n and len(cur) == k:
                lst.append(cur.copy())
                return
            elif i == 10 or cur_sum > n or len(cur) > k:
                return

            backtracking(cur + [i], i + 1, cur_sum + i)
            backtracking(cur, i + 1, cur_sum)



        def backtracking2(cur, i, cur_sum):
            if cur_sum == n and len(cur) == k:
                lst.append(cur.copy())
                return
            elif i > 9 or cur_sum > n or len(cur) > k:
                return
            
            for x in range(i, 10):
                cur.append(x)
                backtracking(cur, x + 1, cur_sum + x)
                cur.pop()

        backtracking2([], 1, 0)
        return lst

# @lc code=end

