class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        #Create an adjacency matrix to log distances from each city 
        max = 10**4 + 1  
        dist = [[max] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        
        #Populate the matrix with the distancse between each node
        for x, y, z in edges:
            dist[x][y] = z
            dist[y][x] = z
        
        #compute shortest paths between each city
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        #count the number of reachable cities
        minimum = n
        result = -1
        
        for i in range(n):
            reachable_cities = 0
            for j in range(n):
                if dist[i][j] <= distanceThreshold:
                    reachable_cities += 1
            
            if reachable_cities < minimum or (reachable_cities == minimum and i > result):
                minimum = reachable_cities
                result = i
        
        return result
