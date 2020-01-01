class Solution:
    # taking advantage of of the fact that num < 3999
    def intToRoman(self, num):
        vals = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90,
                'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
        roman = ''

        for k, v in vals.items():
            while num >= v:
                roman += k
                num -= v
            if num == 0:
                return roman
