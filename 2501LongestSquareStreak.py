from typing import List

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_streak = 0
        
        for num in nums:
            streak_length = 0
            while num in num_set:
                streak_length += 1
                num = pow(num, 2)
            
            if streak_length > max_streak:
                max_streak = streak_length
        
        if max_streak <= 1:
            max_streak = -1
        
        return max_streak

# Test
nums = [4,3,6,16,8,2]
solution = Solution()
print(solution.longestSquareStreak(nums))
