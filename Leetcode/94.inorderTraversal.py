# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def recurseInOrder(self, root, inlist):
        if root.left:
            self.recurseInOrder(root.left, inlist)
        inlist.append(root.val)
        if root.right:
            self.recurseInOrder(root.right, inlist)
        return inlist

    def inorderTraversalRecurse(self, root: TreeNode):
        rtn = []
        if root is None:
            return rtn
        self.recurseInOrder(root, rtn)
        return rtn

    def inorderTraversal(self, root: TreeNode):
        rtn, stack = [], []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                rtn.append(root.val)
                root = root.right
        return rtn
