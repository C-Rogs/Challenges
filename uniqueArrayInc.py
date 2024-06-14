import unittest

class Solution(object):
    def minIncrementForUnique(self, nums):
        nums.sort()
        count = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                diff = nums[i-1] - nums[i] + 1
                nums[i] += diff
                count += diff
        return count
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_min_increment_for_unique(self):
        self.assertEqual(self.s.minIncrementForUnique([3,2,1,2,1,7]), 6)
        self.assertEqual(self.s.minIncrementForUnique([3,3,3,3,3]), 10)
        self.assertEqual(self.s.minIncrementForUnique([1,2,2]), 1)
        self.assertEqual(self.s.minIncrementForUnique([0,2,2]), 1)
        self.assertEqual(self.s.minIncrementForUnique([]), 0)
        self.assertEqual(self.s.minIncrementForUnique([1]), 0)

if __name__ == "__main__":
    unittest.main()