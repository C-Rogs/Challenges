def rob(nums):
        rob, skip = 0, 0
        for n in nums:
            next_rob = skip + n
            next_skip = max(skip, rob)
            rob, skip = next_rob, next_skip
        return max(rob, skip)


def test_rob():
    assert rob([1, 2, 3, 1]) == 4, "Test Case 1 Failed"
    assert rob([2, 7, 9, 3, 1]) == 12, "Test Case 2 Failed"
    assert rob([2, 1, 1, 2]) == 4, "Test Case 3 Failed"
    assert rob([]) == 0, "Test Case 4 Failed"
    assert rob([1]) == 1, "Test Case 5 Failed"
    assert rob([1, 2]) == 2, "Test Case 6 Failed"
    print("All test cases passed")

test_rob()