import unittest

class Solution:
    def romanToIntComp(self, s):
        numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }            
        acc = 0
        for i in range(len(s)-1):
            if numerals[s[i]] < numerals[s[i+1]]:
                acc -= numerals[s[i]]
            else:
                acc += numerals[s[i]]
        return acc + numerals[s[-1]]

    def romanToIntReplace(self, s):
        numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }            
        acc = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
        for symbol in s:
            acc += numerals[symbol]
        return acc
    

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_romanToIntComp(self):
        self.assertEqual(self.solution.romanToIntComp('III'), 3)
        self.assertEqual(self.solution.romanToIntComp('IV'), 4)
        self.assertEqual(self.solution.romanToIntComp('IX'), 9)
        self.assertEqual(self.solution.romanToIntComp('LVIII'), 58)
        self.assertEqual(self.solution.romanToIntComp('MCMXCIV'), 1994)

    def test_romanToIntReplace(self):
        self.assertEqual(self.solution.romanToIntReplace('III'), 3)
        self.assertEqual(self.solution.romanToIntReplace('IV'), 4)
        self.assertEqual(self.solution.romanToIntReplace('IX'), 9)
        self.assertEqual(self.solution.romanToIntReplace('LVIII'), 58)
        self.assertEqual(self.solution.romanToIntReplace('MCMXCIV'), 1994)

if __name__ == '__main__':
    unittest.main()