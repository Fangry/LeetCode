from typing import List

class Solution:
    # DFS
    def permute(self, nums):
        res, origLen = [], len(nums)

        def dfs(count, avail, newPerm):
            if count == origLen:
                return res.append(newPerm)
            for i in range(len(avail)):
                # move onto next layer; generate avail without element at index i; add element at index i
                dfs(count+1, avail[:i] + avail[i+1:], newPerm + [avail[i]])

        dfs(0, nums, [])
        return res

class Solution2:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        lst = []
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        print(d)
        
        def backtracking(cur_d, cur_lst):
            if sum([v for v in cur_d.values()]) == 0:
                lst.append(cur_lst.copy())
            for k in cur_d:
                if cur_d[k] > 0:
                    cur_d[k] -= 1
                    cur_lst.append(k)
                    backtracking(cur_d, cur_lst)
                    cur_d[k] += 1
                    cur_lst.pop()
        
        backtracking(d, [])
        return lst     


s = Solution()
print(s.permute([1, 2, 3]))
