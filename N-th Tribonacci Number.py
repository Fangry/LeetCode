class Solution:
    # this exceeds time limit
    def tribonacci(self, n):
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)

    # more efficient
    def tribonacci2(self, n):
        vals = [0, 1, 1]

        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        for i in range(3, n+1):
            vals.append(vals[i - 1] + vals[i - 2] + vals[i - 3])

        return vals[n]

    # same logic as method 2
    def tribonacci3(self, n):
        a, b, c = 0, 1, 1

        for i in range(n):
            a, b, c = b, c, a + b + c
        return a
