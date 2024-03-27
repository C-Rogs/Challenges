# Complete the 'gridChallenge' function below.
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.

def gridChallenge(grid):
    ordered_grid = list()
    for row in grid:
        row = sorted(list(row))
        ordered_grid.append(row)
    
    for i in range(len(ordered_grid[0])):
        for j in range(len(ordered_grid)-1):
            if ordered_grid[j][i] > ordered_grid[j+1][i]:
                return "NO"
    return "YES"


# Complete the 'minimumBribes' function below.
# The function accepts INTEGER_ARRAY q as parameter.

def minimumBribes(q):
    bribes = 0
    for i in range(len(q)-1, -1, -1):
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribes += 1
    print(bribes)