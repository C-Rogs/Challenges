# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        #make the list a set to increase speed 
        to_delete = set(to_delete)
        
        forest = []  
        def dfs(node):
            if node:
                #call dfs on left and right children until empty
                node.left = dfs(node.left)
                node.right = dfs(node.right)
        
                #If the current node needs to be deleted
                if node.val in to_delete:
                    #Append children to forest if they exist
                    if node.left:
                        forest.append(node.left)
                    if node.right:
                        forest.append(node.right)
                    return None  #delete the current node
                return node  
            return None  #if the node is None, just return None

        if dfs(root) is not None:
            forest.append(root)  #Add the root to the forest if it's not deleted
        
        return forest 