class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        current = 0
        if n == 1:
            return 1


        for i in range(2, n+1):
            current = (k + current) % i
        return current + 1