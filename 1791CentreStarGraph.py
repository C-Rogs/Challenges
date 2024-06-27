class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """

        if edges[1][0] == edges[0][0] or edges[1][0] == edges[0][1]:
            return edges[1][0]
        else:
            return edges[1][1]