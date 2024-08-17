class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        """
        This function calculates the maximum points that can be obtained from a given matrix.
        
        Parameters:
        points (List[List[int]]): A 2D list of integers representing the matrix.
        
        Returns:
        int: The maximum points that can be obtained from the matrix.
        """
        if not points:
            return 0

        x = len(points)
        y = len(points[0])
        a = points[0].copy()

        for i in range(x-1):
            b = [a[0]]

            for j in range(1,y):
                b.append(max(b[-1] -1, a[j]))

            for j in range(y - 2, -1, -1):
                b[j] = max(b[j], b[j +1] -1)

            for j in range(y):
                a[j] = b[j] + points[i+1][j]

        return max(a) if a else 0
