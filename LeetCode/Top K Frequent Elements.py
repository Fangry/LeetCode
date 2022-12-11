from typing import List
#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        buckets = [[] for i in range(len(nums) + 1)]
        for key, v in freq.items():
            buckets[v].append(key)
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            for n in buckets[i]:
                if k == 0:
                    return res
                k -= 1
                res.append(n)
        return res
        
# @lc code=end
sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3], 2))
