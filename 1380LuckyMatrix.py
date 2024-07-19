class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:

        row_mins = [min(row) for row in matrix]
        
        columns = zip(*matrix)
        col_mins = [max(col) for col in columns]
        
        #check for intersections of row mins and column maxes.
        luckys = []
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if val == row_mins[i] and val == col_mins[j]:
                    luckys.append(val)
        
        return luckys