# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree0(self, root: TreeNode) -> TreeNode:
        '''
        翻转一棵二叉树
        '''
        # 当前节点不存在或不存在子节点时返回
        if not root or not (root.left or root.right):
            return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.right)
        self.invertTree(root.left)

        return root

    def invertTree(self, root: TreeNode) -> TreeNode:
        # bfs
        if not root:
            return
        from collections import deque
        q = deque()
        q.appendleft(root)
        while q:
            n = q.pop()
            n.left, n.right = n.right, n.left
            if n.left:
                q.appendleft(n.left)
            if n.right:
                q.appendleft(n.right)
        return root
