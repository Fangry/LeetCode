from typing import List
#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        result = 0
        while l < r:
            volume = (r - l) * min(height[l], height[r])
            if volume > result:
                result = volume
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return result         

        
# @lc code=end

