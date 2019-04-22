# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    '''
    完全二叉树的最小深度
    从根节点到最近叶子节点的最短路径上的节点数量。
    说明: 叶子节点是指没有子节点的节点。
    '''

    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left and root.right:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        elif root.left is not None:
            return 1 + self.minDepth(root.left)
        elif root.right is not None:
            return 1 + self.minDepth(root.right)
        else:
            return 1

    def minDepthFast(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        t = [[root]]
        print(t[-1])
        n = 1
        while True:
            tt = []
            for i in t[-1]:
                if not i.left and not i.right:
                    return n
                if i.left:
                    tt.append(i.left)
                if i.right:
                    tt.append(i.right)
            n += 1
            t.append(tt)
