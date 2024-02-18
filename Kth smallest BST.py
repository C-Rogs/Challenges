class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, lst):
        if not lst:
            return None

        root = cls(lst[0])
        nodes = [root]
        i = 1

        for node in nodes:
            if i < len(lst) and lst[i] is not None:
                node.left = cls(lst[i])
                nodes.append(node.left)
            i += 1

            if i < len(lst) and lst[i] is not None:
                node.right = cls(lst[i])
                nodes.append(node.right)
            i += 1

        return root

class Solution:
    def kthSmallest(self, root, k):
        stack = []
        n = 0
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            curr = curr.right  

class TestSolution:
    def __init__(self):
        self.solution = Solution()

    def run_tests(self):
        root1 = TreeNode(3)
        root1.left = TreeNode(1)
        root1.right = TreeNode(4)
        root1.left.right = TreeNode(2)
        assert self.solution.kthSmallest(root1, 1) == 1, "Test case 1 failed"

        root2 = TreeNode(5)
        root2.left = TreeNode(3)
        root2.right = TreeNode(6)
        root2.left.left = TreeNode(2)
        root2.left.right = TreeNode(4)
        root2.left.left.left = TreeNode(1)
        assert self.solution.kthSmallest(root2, 3) == 3, "Test case 2 failed"

        root3 = TreeNode(1)
        assert self.solution.kthSmallest(root3, 1) == 1, "Test case 3 failed"

        root4 = TreeNode(6)
        root4.left = TreeNode(2)
        root4.right = TreeNode(7)
        root4.left.left = TreeNode(1)
        root4.left.right = TreeNode(4)
        root4.left.right.left = TreeNode(3)
        root4.left.right.right = TreeNode(5)
        assert self.solution.kthSmallest(root4, 3) == 3, "Test case 4 failed"

        print("All test cases passed")




test_solution = TestSolution()
test_solution.run_tests()

