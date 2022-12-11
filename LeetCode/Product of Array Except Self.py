from typing import List
#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = nums.copy()
        # prefix product
        res[0] = 1
        for i in range(1, len(res)):
            res[i] = res[i - 1] * nums[i - 1]
        # postfix product
        postfix_prod = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix_prod
            postfix_prod *= nums[i]
        return res
        
# @lc code=end
sol = Solution()
print(sol.productExceptSelf([1,2,3,4]))
