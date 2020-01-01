class Solution:
    # time limit exceeded but works
    def knightProbability(self, n, k, r, c):
        def helper(r, c, k):
            if r < 0 or r >= n or c < 0 or c >= n:
                return 0
            elif k == 0:
                return 1

            output = 0
            for y, x in [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]:
                output += helper(r + y, c + x, k - 1)
            return output/8

        return helper(r, c, k)

    # dp = result after k steps; dp2 = result after k-1 steps
    def knightProbability2(self, n, k, r, c):
        dp = [[0] * n for i in range(n)]
        dp[r][c] = 1

        # for each step, make an empty dp2, this allows faster computation for each step
        for i in range(k):
            dp2 = [[0] * n for i in range(n)]

            # for each row and col in dp, try all 8 different moves
            for r, row in enumerate(dp):
                for c, val in enumerate(row):
                    for dr, dc in ((2,1),(2,-1),(-2,1),(-2,-1),
                                   (1,2),(1,-2),(-1,2),(-1,-2)):
                        if 0 <= r + dr < n and 0 <= c + dc < n:
                            dp2[r+dr][c+dc] += val / 8
            dp = dp2

        return sum(map(sum, dp))


s = Solution()
print(s.knightProbability2(8, 30, 6, 4))
