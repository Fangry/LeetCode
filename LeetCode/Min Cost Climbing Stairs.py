class Solution:

    # works & intuitive, forward traverse, but didn't use dp, so time limit exceeded
    # then I tried to add memoization to this function, I realize that it's useless 
    # unless you traverse backwards because you never gonna use the previous results 
    # when you are always traversing forward
    def minCostClimbingStairs(self, cost):

        def helper(steps, total):
            if steps == len(cost):
                return total
            elif steps == len(cost)-1:
                return total+cost[steps]
            else:
                newTotal = total + cost[steps]
                return min(helper(steps+1, newTotal),
                           helper(steps+2, newTotal))

        return min(helper(0, 0), helper(1, 0))

    # added dp. forward traverse
    def minCostClimbingStairs2(self, cost):
        a, b = cost[0], cost[1]
        for i in range(2, len(cost)):
            a, b = b, min(a, b) + cost[i]
        return min(a, b)


s = Solution()
print(s.minCostClimbingStairs2([10, 15, 20]))
print(s.minCostClimbingStairs2([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
