import time
import random
   
#brute force 
def minKBitFlipsBrute(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    
    result = 0     
    for i in range(len(nums)):
        if i+k <= len(nums) and nums[i] == 0:
            result += 1
            for n in range(k):
                if nums[i+n] == 0:
                    nums[i+n] = 1
                else: 
                    nums[i+n] = 0
        if i+k > len(nums) and nums[i] == 0:
            result = -1
            break
    return result 

#Sliding window linear time constant space 
def minKBitFlips(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    
    current, result = 0, 0

    for i in range(len(nums)):
        if i >= k and nums[i-k] == 2:
            current -= 1
        if (current % 2) == nums[i]:
            if i+k > len(nums):
                return -1 
            nums[i] = 2
            current +=1 
            result +=1
    return result
    
    # Testing with fixed test cases
print(minKBitFlips([0, 1, 0, 1, 0, 1, 1, 0], 3))  # Expected output: -1
print(minKBitFlips([0, 0, 0, 1, 0, 1, 1, 0], 3))  # Expected output: 3
print(minKBitFlips([0, 1, 0, 1, 0, 1, 1, 0], 4))  # Expected output: -1

# Performance testing with large inputs
start_time = time.time()
large_nums = [random.randint(0, 1) for _ in range(1000000)]
print(minKBitFlips(large_nums, 3))
end_time = time.time()
print("Execution time for large input: ", end_time - start_time)