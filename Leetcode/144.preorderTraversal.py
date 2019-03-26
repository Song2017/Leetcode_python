# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    '''
    给定一个二叉树，返回它的 前序 遍历。
    '''

    def preorderTraversalO(self, root: TreeNode):
        rtn, stack = [], []
        while root or stack:
            if root:
                stack.append(root)
                # 先遍历父节点, 再获取左结点, 最后取右节点
                rtn.append(root.val)
                root = root.left
            else:
                root = stack.pop()
                root = root.right
        return rtn

    def preorderTraversal(self, root: TreeNode):
        if root is None:
            return []
        rtn, stack = [], [root]
        while stack:
            root = stack.pop()
            rtn.append(root)
            # pop: 先弹出后入的元素
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        return rtn
