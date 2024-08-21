class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen = {*{}}
        result = []
        for i in nums: 
            if i in seen:
                result.append(i)
            seen.add(i)
        return result