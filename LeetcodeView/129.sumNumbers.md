# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumNumsR(self, root, s):
        if root is None:
            return 0
        s = s * 10 + root.val
        if not root.left and not root.right:
            return s
        return self.sumNumsR(root.left, s) + self.sumNumsR(root.right, s)

    def sumNumbers0(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return self.sumNumsR(root, 0)

    def sumNumbersF(self, root: TreeNode) -> int:
        def sumNumsInR(root, s):
            if not root:
                return 0
            s = s + root.val
            if not root.left and not root.right:
                return s
            return sumNumsInR(root.left, s * 10) + \
                sumNumsInR(root.right, s * 10)

        return sumNumsInR(root, 0)

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sum = 0

        def dfs(root, pathsum):
            if root:
                pathsum += root.val
                left = dfs(root.left, pathsum * 10)
                right = dfs(root.right, pathsum * 10)
                if not left and not right:
                    self.sum += pathsum
                return True

        dfs(root, 0)
        return self.sum
