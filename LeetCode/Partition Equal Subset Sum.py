from typing import List
#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = {0}
        target = sum(nums) / 2
        if not target.is_integer():
            return False
        for n1 in nums:
            for n2 in s.copy():
                new = n1 + n2
                if new == target:
                    return True
                s.add(new)
        return False
        
# @lc code=end
sol = Solution()
print(sol.canPartition([1,5,11,5]))
