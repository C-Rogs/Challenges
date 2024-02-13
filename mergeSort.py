    
def merge(nums1, m, nums2, n):
        a = m - 1
        b = n - 1
        i = m + n - 1

        while b >= 0:
            #print(nums1)
            if a >= 0 and nums1[a] > nums2[b]:
                nums1[i] = nums1[a]
                a -= 1
            else:
                nums1[i] = nums2[b]
                b -= 1
            i -= 1

# Test cases
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
expected_output = [1, 2, 2, 3, 5, 6]
print(nums1 == expected_output)

nums1 = [1]
m = 1
nums2 = []
n = 0
merge(nums1, m, nums2, n)
expected_output = [1]
print(nums1 == expected_output)

nums1 = [0]
m = 0
nums2 = [1]
n = 1
merge(nums1, m, nums2, n)
expected_output = [1]
print(nums1 == expected_output)