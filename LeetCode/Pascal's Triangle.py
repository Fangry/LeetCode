class Solution:
    def generate(self, numRows):
        triangle = []
        for i in range(numRows):
            # produces a triangle full of None (making the skeleton)
            row = [None for i in range(i+1)]
            # replaces first and lasst None of each row with 1
            row[0], row[-1] = 1, 1

            # fill in the rest of the skeleton
            for j in range(1, len(row)-1):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            triangle.append(row)
        return triangle


s = Solution()
print(s.generate(5))
