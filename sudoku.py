import unittest

class Solution(object):
    def isValidSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        mMat = [set() for _ in range(9)]
            
        for i in range(9):
            for j in range(9):
                cur = board[i][j]
                if cur != '.':
                    k = (i // 3) * 3 + j // 3
                    if cur in rows[i] or cur in cols[j] or cur in mMat[k]: 
                        return False
                    rows[i].add(cur)
                    cols[j].add(cur)
                    mMat[k].add(cur)
        return True
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_empty_board(self):
        board = [["."]*9 for _ in range(9)]
        self.assertTrue(self.s.isValidSudoku(board))

    def test_duplicate_in_row(self):
        board = [
          ["5","5",".",".","7",".",".",".","."],
          ["6",".",".","1","9","5",".",".","."],
          [".","9","8",".",".",".",".","6","."],
          ["8",".",".",".","6",".",".",".","3"],
          ["4",".",".","8",".","3",".",".","1"],
          ["7",".",".",".","2",".",".",".","6"],
          [".","6",".",".",".",".","2","8","."],
          [".",".",".","4","1","9",".",".","5"],
          [".",".",".",".","8",".",".","7","9"]
        ]
        self.assertFalse(self.s.isValidSudoku(board))

    def test_duplicate_in_column(self):
        board = [
          ["5","3",".",".","7",".",".",".","."],
          ["5",".",".","1","9","5",".",".","."],
          [".","9","8",".",".",".",".","6","."],
          ["8",".",".",".","6",".",".",".","3"],
          ["4",".",".","8",".","3",".",".","1"],
          ["7",".",".",".","2",".",".",".","6"],
          [".","6",".",".",".",".","2","8","."],
          [".",".",".","4","1","9",".",".","5"],
          [".",".",".",".","8",".",".","7","9"]
        ]
        self.assertFalse(self.s.isValidSudoku(board))

    def test_duplicate_in_sub_box(self):
        board = [
          ["5","3",".",".","7",".",".",".","."],
          ["6",".",".","1","9","5",".",".","."],
          [".","9","8",".",".",".",".","6","."],
          ["8",".",".",".","6",".",".",".","3"],
          ["4",".",".","8",".","3",".",".","1"],
          ["7",".",".",".","2",".",".",".","6"],
          [".","6",".",".",".",".","2","8","."],
          [".",".",".","5","1","9",".",".","5"],
          [".",".",".",".","8",".",".","7","9"]
        ]
        self.assertFalse(self.s.isValidSudoku(board))

if __name__ == '__main__':
    unittest.main()