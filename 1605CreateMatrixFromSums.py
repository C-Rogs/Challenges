class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        x = min(rowSum, colSum)

        xlen = len(rowSum)
        ylen = len(colSum)
        matrix = [[0] * ylen for i in range(xlen)]

        for x in range(xlen):
            for y in range(ylen):
                matrix[x][y] = min(rowSum[x], colSum[y])
                rowSum[x] -= matrix[x][y]
                colSum[y] -= matrix[x][y]
            #print(matrix)
        return matrix