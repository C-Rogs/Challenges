class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def inOrder(root):
            if root is None: 
                return None 

            inOrder(root.left)
            sorted_nodes.append(root)
            inOrder(root.right)

        def topDownBalancedBST(sorted_nodes):
            if len(sorted_nodes) == 0: 
                return

            mid = len(sorted_nodes) // 2 
            root = sorted_nodes[mid]

            root.left = topDownBalancedBST(sorted_nodes[:mid])
            root.right = topDownBalancedBST(sorted_nodes[mid+1:])

            return root

        sorted_nodes = []  
        inOrder(root)
        
        return topDownBalancedBST(sorted_nodes)

# Tests
# Test case: Unbalanced binary tree
root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(4)

sol = Solution()
new_root = sol.balanceBST(root)
print(new_root.val)  # Expected output: 2
print(new_root.left.val)  # Expected output: 1
print(new_root.right.val)  # Expected output: 4

# Test case: Already balanced binary tree
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

sol = Solution()
new_root = sol.balanceBST(root)
print(new_root.val)  # Expected output: 2
print(new_root.left.val)  # Expected output: 1
print(new_root.right.val)  # Expected output: 3