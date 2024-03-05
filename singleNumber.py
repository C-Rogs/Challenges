def singleNumber( nums):
        ones = 0
        twos = 0
        for num in nums:
            
            #1s  = 1s XOR num and not 2s
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        return ones

if __name__ == "__main__":
    # Test case 1: Empty input list
    assert singleNumber([]) == 0

    # Test case 2: Single number in the list
    assert singleNumber([42]) == 42

    # Test case 3: All duplicate numbers
    assert singleNumber([5, 5, 5, 0]) == 0

    # Test case 4: Multiple duplicate numbers with a single non-duplicate number
    assert singleNumber([2, 2, 3, 2]) == 3

    # Test case 5: Large input list with random numbers
    assert singleNumber([100, 200, 300, 100, 200, 300, 100, 200, 300, 500]) == 500

    # Test case 6: Negative numbers
    assert singleNumber([-1, -1, -1, -3]) == -3

    # Test case 7: Mix of positive and negative numbers
    assert singleNumber([1, 1, 1, -2, -2, -2, -3]) == -3

    print("All test cases passed!")