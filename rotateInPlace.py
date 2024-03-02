class Solution:
    def rotate(self, matrix):
        start = 0 
        end = len(matrix) - 1

        while start < end: 
            matrix[start], matrix[end] = matrix[end], matrix[start]
            start += 1
            end -= 1

        for column in range(len(matrix)):
            for row in range(column):
                matrix[column][row],matrix[row][column] = matrix[row][column],matrix[column][row]

def test_rotate():
    solution = Solution()

    #2x2 matrix
    matrix = [[1, 2], [3, 4]]
    solution.rotate(matrix)
    assert matrix == [[3, 1], [4, 2]], "Test case 1 failed"

    #3x3 matrix
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    solution.rotate(matrix)
    assert matrix == [[7, 4, 1], [8, 5, 2], [9, 6, 3]], "Test case 2 failed"

    #4x4 matrix
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    solution.rotate(matrix)
    assert matrix == [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]], "Test case 3 failed"

    #1x1 matrix
    matrix = [[1]]
    solution.rotate(matrix)
    assert matrix == [[1]], "Test case 4 failed"

    #empty matrix
    matrix = []
    solution.rotate(matrix)
    assert matrix == [], "Test case 5 failed"

test_rotate()
