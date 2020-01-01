class Solution:
    def letterCasePermutation(self, s):
        output = []
        l = len(s)

        def dfs(count, curr):
            if count == l:
                output.append(curr)
            else:
                if curr[count].isalpha():
                    if s[count].isupper():
                        dfs(count+1, curr[:count] + curr[count].lower() + curr[count+1:])
                    else:
                        dfs(count+1, curr[:count] + curr[count].upper() + curr[count+1:])
                dfs(count+1, curr)

        dfs(0, s)
        return output


s = Solution()
print(s.letterCasePermutation("abcd"))
