class Solution(object):
    def searchRangeLinear(self, nums, target):
        output = [-1,-1]
        i = 0
        length = len(nums)
        while i < length:
            if nums[i] == target:
                output[0] = i
                break
            i += 1
        i = length - 1
        while i > -1:
            if nums[i] == target:
                output[1] = i
                break
            i -= 1
        return output

class Tests:
    @staticmethod
    def run():
        solution = Solution()

        nums = [5, 7, 7, 8, 8, 10]
        target = 8
        assert solution.searchRangeLogarithmic(nums, target) == [3, 4], "Test case 1 failed"

        nums = [5, 7, 7, 8, 8, 10]
        target = 6
        assert solution.searchRangeLogarithmic(nums, target) == [-1, -1], "Test case 2 failed"

        nums = []
        target = 0
        assert solution.searchRangeLogarithmic(nums, target) == [-1, -1], "Test case 3 failed"

        nums = [2, 2, 2, 2, 2]
        target = 2
        assert solution.searchRangeLogarithmic(nums, target) == [0, 4], "Test case 4 failed"

        nums = [1, 3, 5, 7, 9]
        target = 7
        assert solution.searchRangeLogarithmic(nums, target) == [3, 3], "Test case 5 failed"
        print("All test cases passed")

Tests.run()
