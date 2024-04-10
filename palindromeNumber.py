class Solution(object):
    def isPalindromeString(self, x):
        if x < 0:
            return False
        if str(x) == str(x)[::-1]:
            return True 


    def isPalindrome(self, x):
        if x < 0 or (x > 0 and x%10 == 0):
            return False

        result = 0
        while x > result:
            result = result * 10 + x % 10
            x = x // 10
        return True if (x == result or x == result // 10) else False