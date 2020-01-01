class Solution:

    # no dp, time limit didn't exceed but encountered: recursionError (max. recursion depth exceeded)
    def isSubsequence(self, s, t):

        if s == '':
            return True
        elif len(s) > len(t):
            return False

        def helper(i, curr):
            if s == curr:
                return True
            elif curr not in s or i >= len(t):
                return False
            else:
                return helper(i+1, curr+t[i]) or helper(i+1, curr)

        return helper(0, '')

    # no dp, simple loop, time complexity O(n)
    def isSubsequence2(self, s, t):
        # pointers for both s & t
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)


s = Solution()
print(s.isSubsequence2('', 'ahbgdc'))
print(s.isSubsequence2('abc', ''))
print(s.isSubsequence2('abc', 'ahbgdc'))
print(s.isSubsequence2('axc', 'ahbgdc'))
print(s.isSubsequence2('twn', 'xtxwxn'))
