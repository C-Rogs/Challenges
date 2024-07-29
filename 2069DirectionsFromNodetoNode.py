#Did not complete in time - refine.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def findPath(node, target):
                if not node:
                    return None
                if node.val == target:
                    return []
                left_path = findPath(node.left, target)
                if left_path is not None:
                    return ['L'] + left_path
                right_path = findPath(node.right, target)
                if right_path is not None:
                    return ['R'] + right_path
                return None

        #Paths from the root to startValue and destValue
        start_path = findPath(root, startValue)
        dest_path = findPath(root, destValue)
        #print("Start path:", start_path)
        #print("Destination path:", dest_path)

        while len(start_path) and len(dest_path) and start_path[-1] == dest_path[-1]:
            start_path.pop()
            dest_path.pop()
        return "".join("U" * len(start_path)) + "".join(reversed(dest_path))

        #Work out where the paths diverge 
        i = 0
        while i < len(start_path) and i < len(dest_path) and start_path[i] == dest_path[i]:
            i += 1

        #Join up the upjumps and remaning moves to destination. 
        up_jumps = 'U' * (len(start_path) - i)
        down_jumps = ''.join(dest_path[i:])
        return up_jumps + down_jumps

        