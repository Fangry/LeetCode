class Solution:
    # O(n^2) time
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    # O(n) time, this works by storing the value needed and its index in a dictionary
    def twoSum2(self, nums, target):
        d = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in d:
                return [d[m], i]
            else:
                d[n] = i


s = Solution()
# print(s.twoSum([2, 7, 11, 15], 9))
print(s.twoSum2([3, 2, 4], 6))
