class Solution:
    #faster
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        
        for i in range(len(nums)):
            negative = target - nums[i]
            if negative in hash:
                return [hash[negative],i]
            hash[nums[i]] = i
        
        return [0,0]
    
    