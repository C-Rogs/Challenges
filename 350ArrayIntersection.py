class Solution(object):
    def intersect(self, nums1, nums2):
       
        nums1.sort()
        nums2.sort()

        print(nums1)
        print(nums2)
        result = []
        
        a, b = 0, 0

        while a < len(nums1) and b < len(nums2):
            if nums1[a] < nums2[b]:
                a += 1
            elif nums1[a] > nums2[b]:
                b += 1
            else:
                result.append(nums1[a])
                a += 1
                b += 1
        return result