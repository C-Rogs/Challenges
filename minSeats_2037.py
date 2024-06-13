class Solution:
    # This uses a greedy strategy moving the student to the closest (locally optimal) seat.
    def minMovesToSeat(self, seats, students):
        seats.sort()
        students.sort()
        
        moves = 0
        for i in range(len(seats)):
            while seats[i] != students[i]:
                if seats[i] > students[i]:
                    students[i] += 1
                else: 
                    students[i] -= 1
                moves += 1
        return moves
        
# Driver code
solution = Solution()

# Test cases
print(solution.minMovesToSeat([3,1,5], [2,7,4])) #=4
print(solution.minMovesToSeat([4,1,5,9], [1,5,9,4])) #=0
print(solution.minMovesToSeat([1,2,3], [3,2,1])) #=0
print(solution.minMovesToSeat([3,3,1,3], [1,2,2,2])) #=3
