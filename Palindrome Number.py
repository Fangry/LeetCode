class Solution:
    # version 1
    def isPalindrome(self, x):
        xStr = str(x)
        xStrRev = xStr[::-1]
        for i in range(len(xStr)):
            if xStr[i] is not xStrRev[i]:
                return False
        return True

    # version 2
    def isPalindrome2(self, x):
        return str(x) == str(x)[::-1]

    # version 3 (without converting int to str)
    def isPalindrome3(self, x):
        # a negative sign in front can never be a palindrome
        # also, if the last digit is 0 and the number itself isn't 0 then it's not a palindrome
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        # build the reverse of the first half of x
        revNum = 0
        while x > revNum:
            revNum = revNum * 10 + x % 10
            x = int(x/10)

        # revNum / 10 takes care of the case when revNum is odd (ex. 123), it gets rid of the last digit
        return x == revNum or x == revNum / 10

    def isPalindrome4(self, x):
        xStr = str(x)
        xRevStr = ""
        for c in xStr:
            xRevStr = c + xRevStr
        if xStr == xRevStr:
            return True
        else:
            return False
