class Solution:
    def minDifference(self, nums: List[int]) -> int:
        #Any value can be matched if fewer than five digits.
        if len(nums) <= 4:
            return 0
        
        nums.sort()

        # There are four situations which could then happen:
        a = nums[-4] - nums[0] #4th largest - smallest (imagine all 3 largest removed)
        b = nums[-1] - nums[3] #largest - 4th smallest 
        c = nums[-3] - nums[1] #3rd largest - 2nd smallest
        d = nums[-2] - nums[2] #2nd largest - 3rd smallest 
        
        return min(a,b,c,d)
        