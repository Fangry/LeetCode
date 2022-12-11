from typing import List
#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < len(numbers) and r >= 0:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l + 1, r + 1]
            elif s > target:
                r -= 1
            else:
                l += 1
        return []
        
# @lc code=end
sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))
