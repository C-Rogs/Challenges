# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def __init__(self):
        self.sum = 0
    def bstToGst(self, root):
        if root:
            self.bstToGst(root.right)  #Move to the right tree below node 
            self.sum += root.val  #Keep track of the value of the nodes visited
            root.val = self.sum  #Record the running total for the current node
            self.bstToGst(root.left)  #Now check if there is anything in the left tree
        return root