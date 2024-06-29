import collections

class Solution(object):
    def getAncestors(self, n, edges):
        """
        This function takes a number 'n' and a list of edges and 
        returns a list of ancestors for each node.

        :param n: int, Number of nodes
        :param edges: List[List[int]], List of edges
        :return: List[List[int]], List of ancestors for each node
        """
        
        # Initialize an empty dictionary for the graph and the ancestors
        graph = {}
        result = [[] for i in range(n)]  # Initialize list with 'n' empty lists

        # Loop over edges. For each edge, add the start node to the end node's list in the graph
        for a, b in edges:
            graph[b] = graph.get(b, []) + [a]

        # Loop over the nodes in the graph
        for a in graph:
            # Initialize visited set and paths list with the current node
            visited = set()
            paths = [a]

            # Loop while there are nodes in the paths list
            while len(paths) > 0:
                # Pop a node from the paths list
                curr = paths.pop()
                # For each of the popped node's neighbors
                for b in graph.get(curr, []):
                    # If the neighbor hasn't been visited yet
                    if b not in visited:
                        # Add it to the visited set and the paths list
                        visited.add(b)
                        paths.append(b)
            # Sort the visited nodes and add them to the result list
            result[a] = sorted(visited)

        # Return the result list
        return result