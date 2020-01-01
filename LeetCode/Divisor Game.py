class Solution:
    '''
    If you draw the dicision tree out for each n, you will see that this is the case
    Whoever gets 1 loses 
    Whoever gets 2 wins, so it's a fight for 2

    When n is even, Alice can always choose 1 
    Bob will then have to choose divisor of an odd number
    Since divisors of odd number are all odd, Alice will get an even number again
    So this process repeats & assuming Alice makes no mistake, Bob will always end up on n = 3
    Thus Alices always wins on even
    '''

    def divisorGame(self, n):
        return n % 2 == 0

    # using dp
    def divisorGame2(self, n):
        dp = [False for i in range(n+1)]

        for i in range(n+1):
            # range only goes up to i//2 + 1 because you will repeat divisors
            for j in range(1, i//2 + 1):
                # dp[i-j] represents whether Bob wins the game
                if i % j == 0 and (not dp[i - j]):
                    # Alice wins for number i
                    dp[i] = True
                    break
        
        # whether Alice wins the game
        return dp[n]


s = Solution()
print(s.divisorGame2(8))
# for i in range(1, 10):
#     print(s.divisorGame2(i))
