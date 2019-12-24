class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] + nums[j] == target:
                    print([i, j])

