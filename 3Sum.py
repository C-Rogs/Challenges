def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums.sort()
    solutions = []

    for i in range(len(nums) - 2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i-1]:
            continue

        left, right = i + 1, len(nums) - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum > 0:
                right -= 1
            elif current_sum < 0:
                left += 1
            else:
                solutions.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return solutions

assert threeSum([0, 0, 0]) == [[0, 0, 0]]
assert threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
assert threeSum([]) == []
assert threeSum([1, 2, -2, -1]) == []
assert threeSum([-2, 0, 1, 1, 2]) == [[-2, 0, 2], [-2, 1, 1]]