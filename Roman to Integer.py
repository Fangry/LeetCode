class Solution:
    def romanToInt(self, s):
        vals = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000}

        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return vals[s[0]]

        sum, i = 0, 0
        while i < len(s):
            curr = vals[s[i]]
            if i == len(s) - 1:
                 sum += curr
                 i += 1
            else:
                next = vals[s[i+1]]
                if curr >= next:
                    sum += curr
                    i += 1
                else:
                    sum += next - curr
                    i += 2
        
        return sum

