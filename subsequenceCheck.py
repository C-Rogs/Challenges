import unittest

class Solution(object):
    def isSubsequenceA(self, s, t):
        sub=0
        s_length = len(s)
        t_length = len(t)

        if s_length > t_length:
            return False
        if s_length == 0:
            return True

        for i in range(0,t_length):
            if sub <= len(s)-1 and s[sub]==t[i]:
                sub += 1
        return  sub == len(s) 
    
    def isSubsequence(self, s, t):
        s_length = len(s)
        t_length = len(t)
        if s_length > t_length:
            return False
        #The following snippet requires the above snippet to handle cases where s>t. 
        t = iter(t)
        return all(c in t for c in s)
    

class TestIsSubsequence(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        self.assertEqual(self.solution.isSubsequence('abc', 'ahbgdc'), True)

    def test_case_2(self):
        self.assertEqual(self.solution.isSubsequence('axc', 'ahbgdc'), False)

    def test_case_3(self):
        self.assertEqual(self.solution.isSubsequence('', 'ahbgdc'), True)

    def test_case_4(self):
        self.assertEqual(self.solution.isSubsequence('ahbgdc', ''), False)

    def test_case_5(self):
        self.assertEqual(self.solution.isSubsequence('', ''), True)

if __name__ == '__main__':
    unittest.main()