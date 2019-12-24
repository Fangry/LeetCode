class Solution:
    # method 1: vertical scanning
    def longestCommonPrefix(self, strs):
        if strs == []:
            return ""
        if len(strs) == 1:
            return strs[0]

        prefix = ""
        shortestLen = len(min(strs, val=len))
        for i in range(shortestLen):
            for j in range(len(strs) - 1):
                if strs[j][i] != strs[j + 1][i]:
                    return prefix
            prefix += strs[0][i]
        return prefix

    # method 2: better vertical scanning
    def longestCommonPrefix2(self, strs):
        if strs == []:
            return ""

        prefix = ""
        for i in range(len(min(strs))):
            curr = strs[0][i]
            if all(a[i] == curr for a in strs):
                prefix += curr
            else:
                break
        return prefix

    # method 3: horizontal scanning
    def longestCommonPrefix3(self, strs):
        if strs == []:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        prefix = strs[0]
        for i in range(1, len(strs)):
            temp = ""
            for j in range(len(min(prefix, strs[i], val=len))):
                if prefix[j] == strs[i][j]:
                    temp += prefix[j]
                else:
                    prefix = temp
                    break
            prefix = temp
        return prefix
                
s = Solution()
print(s.longestCommonPrefix3(["aa", "a"]))
            
