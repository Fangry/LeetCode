class Solution:

    # without dp, time limit exceeded, time complexity O(2^n)
    def climbStairs(self, n):

        def helper(curr):
            if curr > n:
                return 0
            elif curr == n:
                return 1
            else:
                return helper(curr+1) + helper(curr+2)

        return helper(0)

    # dp: recursion with memoization, time complexity O(n)
    def climbStairs2(self, n):

        def helper(curr, memo):
            if curr > n:
                return 0
            elif curr == n:
                return 1
            elif memo[curr]:
                return memo[curr]
            else:
                memo[curr] = helper(curr+1, memo) + helper(curr+2, memo)
                return memo[curr]

        return helper(0, [None for i in range(n+1)])

    # dp: bottom-up approach, time complexity O(n)
    # key realization: dp[i] = dp[i-1] + dp[i-2], sort of like fibonacci sequence
    def climbStairs3(self, n):
        if n == 1:
            return 1

        a, b = 1, 2
        for i in range(2, n):
            temp = a
            a = b
            b = temp + b
        return b


s = Solution()
# print(s.climbStairs(2))
# print(s.climbStairs(3))
print(s.climbStairs3(35))
