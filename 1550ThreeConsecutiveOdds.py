#One solution to three consecutive odd problem which runs in O(n) time and O(1) space. It skips through ahead 
#   it skips through if the 2nd or 3rd are not odd to save time.

class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        point = 0

        while point < len(arr)-2:
            if arr[point+2] % 2 == 0: 
                point += 3
            elif arr[point+2] % 2 == 0 and arr[point+1] % 2 == 0: 
                point += 2                
            elif arr[point] % 2 != 0 and arr[point+1] % 2 != 0 and arr[point+2] % 2 != 0:
                return True
            point += 1
        return False 