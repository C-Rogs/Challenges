#Sort colours(0,1,2) into order

class Solution:
    
    def sortColors(self, nums):
        red, white, blue = 0, 0, len(nums)-1

        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
        return nums

#get going
s = Solution()

#random test 
nums = [2,0,2,1,1,0]
print(s.sortColors(nums)) # Expected output: [0,0,1,1,2,2]

#smallest edge case 
nums = [2,0,1]
print(s.sortColors(nums)) # Expected output: [0,1,2]

#half sorted 
nums = [0,0,1,2,2,1]
print(s.sortColors(nums)) # Expected output: [0,0,1,1,2,2]