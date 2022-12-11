from typing import List
#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def convert_to_hashmap(s):
            hash = {}
            for c in s:
                if c in hash:
                    hash[c] += 1
                else:
                    hash[c] = 1
            return hash
        anagram_lst = [convert_to_hashmap(s) for s in strs]
        result_lst = []
        for i in range(len(anagram_lst)):
            if anagram_lst[i] == None:
                continue
            new_sub_lst = [strs[i]]
            for j in range(i + 1, len(anagram_lst)):
                if anagram_lst[i] == anagram_lst[j]:
                    new_sub_lst.append(strs[j])
                    anagram_lst[j] = None
            anagram_lst[i] = None
            result_lst.extend([new_sub_lst])
        return result_lst
        
# @lc code=end
sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
