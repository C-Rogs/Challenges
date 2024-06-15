import heapq

class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        balance = w
        projects = list(zip(capital, profits))
        projects.sort()
        project_q = []

        i = 0
        for x in range(k):
            while i < len(projects) and projects[i][0] <= balance:
                heapq.heappush(project_q, -projects[i][1])
                i += 1

            if not project_q:
                break
            balance += -heapq.heappop(project_q)
        return balance
    
if __name__ == "__main__":
    s = Solution()

    k = 2
    w = 0
    profits = [1,2,3]
    capital = [0,1,1]

    result = s.findMaximizedCapital(k, w, profits, capital)
    print(f"The final maximized capital is: {result}")