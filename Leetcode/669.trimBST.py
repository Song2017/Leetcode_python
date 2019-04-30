# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def trimBSTM(self, root: TreeNode, L: int, R: int) -> TreeNode:
        def trim(node):
            if not node:
                return None
            if node.val < L:
                return trim(node.right)
            elif node.val > R:
                return trim(node.left)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node

        return trim(root)

    def trimBSTF(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val > R:
            return self.trimBST(root.left, L, R)
        if root.val < L:
            return self.trimBST(root.right, L, R)
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        return root

    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        while root.val < L or root.val > R:
            if root.val < L:
                root = root.right
            else:
                root = root.left

        while root:
            if root.val > L:
                root = root.left

        return root
