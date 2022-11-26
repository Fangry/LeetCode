#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#
from typing import List

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_product = nums[0]
        min_product = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            temp = max_product
            max_product = max(nums[i], max_product * nums[i], min_product * nums[i])
            min_product = min(nums[i], temp * nums[i], min_product * nums[i])
            result = max(result, max_product)
        return result
        
# @lc code=end
s = Solution()
print(s.maxProduct([3, 3, 0, 1, 1]))
