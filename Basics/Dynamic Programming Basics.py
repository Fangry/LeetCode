# not DP, exponential run time (bad)
def fib_recursive(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)


'''
DP = recursion + memoization ***
   = careful brute force
   = split a problem into subproblems & reuse their solutions

fib(k) should only recurses the first time it's called for all k, 
the first time you encounter k the recursion does work and every time after that
memoized (non-recursive) calls cost O(1), basically free

We only need to pay for fib(1), fib(2) ... fib(k)
Which is O(n)
'''


'''
Three Steps to DP:
1. recursion
2. store intermediate computations (memoize, not memorize)
3. come up with  a bottom-up approach
'''


# memoized solution, time complexity O(n)
def fib_memo(n):
    memo = [None for i in range(n+1)]

    def helper(n, memo):
        if memo[n]:
            return memo[n]
        if n == 1 or n == 2:
            result = 1
        else:
            result = helper(n-1, memo) + helper(n-2, memo)
        memo[n] = result
        return result

    return helper(n, memo)


# same idea as fib_memo
def fib_memo2(n):
    memo = [0, 1]

    while len(memo) < n + 1:
        memo.append(0)

    if n <= 1:
        return n
    else:
        if memo[n - 1] == 0:
            memo[n - 1] = fib_memo2(n - 1)

        if memo[n - 2] == 0:
            memo[n - 2] = fib_memo2(n - 2)

    memo[n] = memo[n - 2] + memo[n - 1]
    return memo[n]


# same idea as fib_memo2, but use two numbers instead of list, bottom-up approach
# Still linear time, but CONSTANT SPACE
def fib_memo3(n):
    a, b = 0, 1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
        return b
