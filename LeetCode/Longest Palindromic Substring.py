#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # DP
        n = len(s)
        t = [[0 for j in range(n)] for i in range(n)]
        res = ''
        # palindrome of length 1
        for i in range(n):
            t[i][i] = 1
            res = s[i]
        # palindrome of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                t[i][i + 1] = 1
                res = s[i:i + 2]
            else:
                t[i][i + 1] = 0
        # palindrome of length > 2
        for i in range(n):
            for j in range(i + 2, n):
                x = j - i - 2
                y = j
                # print(x, y)
                # print(s[x], s[y], t[x + 1][y - 1])
                if s[x] == s[y] and t[x + 1][y - 1] == 1:
                    t[x][y] = 1
                    if y - x + 1 > len(res):
                        res = s[x:y+1]

        # for i in range(n):
        #     for j in range(n):
        #         print(t[i][j], end='')
        #     print()
        # print(res)

        return res

# @lc code=end
s = Solution()
s.longestPalindrome("babad")
