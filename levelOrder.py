import unittest

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class SolutionRecursive:
    def levelOrder(self, root: TreeNode):
        result = []
        def bfs(node,i):
            if node:
                if i < len(result):
                    result[i].append(node.val)
                else:
                    result.append([node.val])
                
                i += 1
                bfs(node.left, i)
                bfs(node.right, i)
        bfs(root, 0)
        return result
    
class SolutionIterative:
    def levelOrder(self, root:TreeNode):
        if not root:
            return []
        result = []
        queue = [root]

        while queue:
            next_queue = []
            level = []
            for root in queue:
                level.append(root.val)
                if root.left:
                    next_queue.append(root.left)
                if root.right:
                    next_queue.append(root.right)

            result.append(level)
            queue = next_queue

        return result

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.root1 = TreeNode(1)
        self.root1.left = TreeNode(2)
        self.root1.right = TreeNode(3)
        self.root1.left.left = TreeNode(4)
        self.root1.left.right = TreeNode(5)

        self.root2 = TreeNode(6)
        self.root2.left = TreeNode(7)
        self.root2.right = TreeNode(8)
        self.root2.left.left = TreeNode(9)
        self.root2.left.right = TreeNode(10)

        #(single node)
        self.root3 = TreeNode(11)

        #(null tree)
        self.root4 = None

    def test_recursive_solution(self):
        sol = SolutionRecursive()

        result1 = sol.levelOrder(self.root1)
        self.assertEqual(result1, [[1], [2, 3], [4, 5]])

        result2 = sol.levelOrder(self.root2)
        self.assertEqual(result2, [[6], [7, 8], [9, 10]])

        result3 = sol.levelOrder(self.root3)
        self.assertEqual(result3, [[11]])

        result4 = sol.levelOrder(self.root4)
        self.assertEqual(result4, [])

    def test_iterative_solution(self):
        sol = SolutionIterative()

        result1 = sol.levelOrder(self.root1)
        self.assertEqual(result1, [[1], [2, 3], [4, 5]])

        result2 = sol.levelOrder(self.root2)
        self.assertEqual(result2, [[6], [7, 8], [9, 10]])

        result3 = sol.levelOrder(self.root3)
        self.assertEqual(result3, [[11]])

        result4 = sol.levelOrder(self.root4)
        self.assertEqual(result4, [])

if __name__ == '__main__':
    unittest.main()