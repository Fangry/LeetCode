class Solution:
    # Time complexity: O(n^2)
    def maxProfit(self, prices):
        maxProfit = 0
        l = len(prices)

        for i in range(l-1):
            for j in range(i+1, l):
                profit = prices[j] - prices[i]
                if profit > maxProfit:
                    maxProfit = profit
        return maxProfit

    # Time complexity O(n)
    def maxProfit2(self, prices):
        minPrice, maxProfit = float('inf'), 0

        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            elif maxProfit < prices[i] - minPrice:
                maxProfit = prices[i] - minPrice
        return maxProfit

    # maxProfit2 simplified
    def maxProfit3(self, prices):
        minPrice, maxProfit = float('inf'), 0

        for p in prices:
            maxProfit = max(maxProfit, p - minPrice)
            minPrice = min(minPrice, p)
        return maxProfit
