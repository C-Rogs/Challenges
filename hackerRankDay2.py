# Complete the 'lonelyinteger' function below.
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
def lonelyinteger(a):
    checked = {}
    for n in a:
        if n in checked:
            checked[n] += 1
        else:
            checked[n] = 0
    for key, value in checked.items():
        if 0 == value:
            return key

def lonelyintegerxor(a):
    result = 0
    for number in a:
        result ^= number
    return result

# Complete the 'diagonalDifference' function below.
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
def diagonalDifference(arr):
    left = right = 0
    for i in range(len(arr)):
        left += arr[i][i]
        right += arr[i][len(arr) - i - 1]
    return abs(left - right)

# Complete the 'countingSort' function below.
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
def countingSort(arr):
    result = [0] * 100
    for i in arr:
        result[i] += 1
    return result

import unittest

class TestFunctions(unittest.TestCase):
    def test_lonelyinteger(self):
        self.assertEqual(lonelyinteger([1, 1, 2]), 2)
        self.assertEqual(lonelyinteger([0, 0, 1, 1, 2]), 2)
        self.assertEqual(lonelyinteger([0]), 0)

    def test_lonelyintegerxor(self):
        self.assertEqual(lonelyintegerxor([1, 1, 2]), 2)
        self.assertEqual(lonelyintegerxor([0, 0, 1, 1, 2]), 2)
        self.assertEqual(lonelyintegerxor([0]), 0)

    def test_diagonalDifference(self):
        self.assertEqual(diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]), 15)
        self.assertEqual(diagonalDifference([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 0)
        self.assertEqual(diagonalDifference([[1]]), 0)

    def test_countingSort(self):
        self.assertEqual(countingSort([1, 2, 3, 2, 1]), [0, 2, 2] + [0]*97)
        self.assertEqual(countingSort([0, 0, 0, 1, 1, 1, 2, 2, 2]), [3, 3, 3] + [0]*97)
        self.assertEqual(countingSort([]), [0]*100)

if __name__ == '__main__':
    unittest.main()