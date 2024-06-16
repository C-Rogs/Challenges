
def minPatches(nums, n):
    """
    :type nums: List[int]
    :type n: int
    :rtype: int
    """
    
    patches = 0
    coverage = 0
    i = 0

    while coverage < n: 
        if i < len(nums) and nums[i] <= coverage + 1: 
            coverage += nums[i]
            i += 1 
        else:
            patches += 1
            coverage += coverage + 1
    return patches
    
print(minPatches([1,4,8],9999))