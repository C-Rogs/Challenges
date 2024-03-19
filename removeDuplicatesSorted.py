
import unittest


class Solution(object):
    def removeDuplicatesPop(self, nums):
        i = 1
        while i < len(nums):
            if nums[i - 1] == nums[i]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)

    def removeDuplicatesTwoPointers(self, nums):
        check = 0
        for i in range(1, len(nums)):
            if nums[check] != nums[i]:
                check += 1
                nums[check] = nums[i]
        return check + 1  # <--- fails on empty lists because it always adds one to the length. 


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_removeDuplicatesPop(self):
        self.assertEqual(self.solution.removeDuplicatesPop([1, 1, 2]), 2)
        self.assertEqual(self.solution.removeDuplicatesPop(
            [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]), 5)
        self.assertEqual(self.solution.removeDuplicatesPop([]), 0)
        self.assertEqual(self.solution.removeDuplicatesPop([1, 2, 3, 4]), 4)

    def test_removeDuplicatesTwoPointers(self):
        self.assertEqual(
            self.solution.removeDuplicatesTwoPointers([1, 1, 2]), 2)
        self.assertEqual(self.solution.removeDuplicatesTwoPointers(
            [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]), 5)
        self.assertEqual(self.solution.removeDuplicatesTwoPointers([]), 0)
        self.assertEqual(
            self.solution.removeDuplicatesTwoPointers([1, 2, 3, 4]), 4)


if __name__ == '__main__':
    unittest.main()
