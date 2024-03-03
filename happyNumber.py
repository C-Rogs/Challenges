class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.getNext(n)  # Calculate the next number in the sequence
        return n == 1

    def getNext(self, n: int) -> int:
        sum_of_squares = 0
        while n > 0:
            digit = n % 10
            sum_of_squares += digit * digit
            n //= 10
        return sum_of_squares
    
# Driver code and test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.isHappy(19) == True
    assert solution.isHappy(4) == False
    assert solution.isHappy(7) == True
    assert solution.isHappy(2) == False
    assert solution.isHappy(100) == True
    print("All test cases passed!")


    """ 
    Recursive way to find Happy number that will run for ever if it isn't. 
    letters = str(n)
    temp_sum = 0
    for i in range(len(letters)):
        temp_sum += int(letters[i])**2
    print(temp_sum)
    if temp_sum == 1:
        return True
    else:
        return self.isHappy(temp_sum)
    """
