# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        if root.val > val:
            if root.left is None:
                root.left = TreeNode(val)
            else:
                self.insertIntoBST(root.left, val)
        elif root.val < val:
            if root.right is None:
                root.right = TreeNode(val)
            else:
                self.insertIntoBST(root.right, val)
        else:
            new = TreeNode(val)
            new.right = root.right
            root.right = new
        return root

    def insertBST(self, root: TreeNode, val: int):
        if root.val > val:
            if root.left is None:
                root.left = TreeNode(val)
            else:
                self.insertBST(root.left, val)
        elif root.val < val:
            if root.right is None:
                root.right = TreeNode(val)
            else:
                self.insertBST(root.right, val)
        else:
            new = TreeNode(val)
            new.right = root.right
            root.right = new

    def insertIntoBST1(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        self.insertBST(root, val)
        return root
