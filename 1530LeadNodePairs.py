# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        #depth first search fucntion 
        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [1]
            left = dfs(node.left)
            right = dfs(node.right)

            #check pairs
            for l in left:
                for r in right:
                    if l + r <= distance:
                        self.result += 1
            
            #collect distances
            current = []
            for d in left + right:
                if d + 1 <= distance:
                    current.append(d + 1)
            return current

        self.result = 0
        dfs(root)
        return self.result