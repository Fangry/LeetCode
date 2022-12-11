#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def convert_to_hashmap(s):
            hash = {}
            for c in s:
                if c in hash:
                    hash[c] += 1
                else:
                    hash[c] = 1
            return hash
        return convert_to_hashmap(s) == convert_to_hashmap(t)
        
# @lc code=end

