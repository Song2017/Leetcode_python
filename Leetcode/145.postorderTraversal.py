# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal0(self, root: TreeNode):
        if root is None:
            return []
        rtn, stack = [], []
        while stack or root:
            if root:
                stack.append(root)
                rtn.insert(0, root.val)
                root = root.right
            else:
                root = stack.pop()
                root = root.left
        return rtn

    def postorder(self, root, lst):
        if root.left:
            self.postorder(root.left, lst)
        if root.right:
            self.postorder(root.right, lst)
        lst.append(root.val)
        return lst

    def postorderTraversalR(self, root: TreeNode):
        if root is None:
            return []
        rtn = []
        self.postorder(root, rtn)
        return rtn

    def postorderTraversalB(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        r = []

        def traversal(_r):
            if not _r:
                return
            traversal(_r.left)
            traversal(_r.right)
            r.append(_r.val)

        traversal(root)
        return r

    def postorderTraversalF(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]

        后序遍历: 左右根
        入栈: 左右
        出栈: 根右左
        结果: 取反
        """
        if root is None:
            return []
        stack, output = [root], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            if root.left is not None:
                stack.append(root.left)
            if root.right is not None:
                stack.append(root.right)

        return output[::-1]
