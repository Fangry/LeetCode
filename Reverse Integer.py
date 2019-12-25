class Solution:
    def reverse1(self, x):
        acc = []

        def helper(x):
            if x == 0:
                total = 0
                for x, y in enumerate(acc):
                    total += pow(10, x) * y
                if total > 2147483647:  # less than 32 bit
                    return 0
                else:
                    return total
            else:
                q, r = divmod(x, 10)
                acc.insert(0, r)
                return helper(q)

        if x < 0:
            return -1 * helper(-1 * x)
        else:
            return helper(x)

    def reverse2(self, x):
        sign = (x > 0) - (x < 0)
        r = int(str(x * s)[::-1])
        return sign * r * (r < 2 ** 31)

s = Solution()

