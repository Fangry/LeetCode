from typing import List
#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        lst = []
        end = len(candidates)

        def backtracking(i, curr_dict, curr_sum):
            if curr_sum == target:
                lst.append(curr_dict)
                return
            if i == end or curr_sum > target:
                return
            temp_dict = curr_dict.copy()
            if candidates[i] not in temp_dict:
                temp_dict[candidates[i]] = 1
            else:
                temp_dict[candidates[i]] += 1
            backtracking(i, temp_dict, curr_sum + candidates[i])
            # backtracking(i + 1, temp_dict, curr_sum + candidates[i])
            backtracking(i + 1, curr_dict, curr_sum)

        backtracking(0, {}, 0)
        for i in range(len(lst)):
            lst[i] = [key for key, value in lst[i].items() for _ in range(value)]
        print(lst)
        return lst
        
# @lc code=end
sol = Solution()
sol.combinationSum([2,3,6,7], 7)
