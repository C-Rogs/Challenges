import unittest

class Solution(object):
    def isPalindrome(self, s):
        s = ''.join(filter(str.isalnum, str(s).lower()))   
        for i in range(len(s)//2):
            if s[i] != s[-i-1]:
                return False           
        return True
    
class Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testCase(self):
        self.assertTrue(self.solution.isPalindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(self.solution.isPalindrome("race a car"))
        self.assertTrue(self.solution.isPalindrome(" "))
        self.assertTrue(self.solution.isPalindrome("12321"))
        self.assertFalse(self.solution.isPalindrome("12345"))

if __name__ == '__main__':
    unittest.main()