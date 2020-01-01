class Solution:
    def subsets(self, nums):
        output = []
        l = len(nums)

        # more intuitive
        def dfs(count, curr):
            if count == l:
                output.append(curr)
            else:
                dfs(count+1, curr + [nums[count]])
                dfs(count+1, curr)

        dfs(0, [])
        return output

    # iterative, less intuitive
    def subsets2(self, nums):
        output = [[]]
        for n in nums:
            for i in range(len(output)):
                # every current subset in output add the next n in nums
                output += [output[i] + [n]]
        return output


s = Solution()
print(s.subsets2([i for i in range(3)]))
