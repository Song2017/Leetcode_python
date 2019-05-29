# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    '''
    给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
    百度百科中最近公共祖先的定义为：
        “对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，
        满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
    '''
    def lowestCommonAncestor0(self, root, p, q):
        def ancestor(root):
            if p.val <= root.val <= q.val:
                return root
            elif root.val > q.val:
                return ancestor(root.left)
            else:
                return ancestor(root.right)

        if p.val > q.val:
            p, q = q, p
        return ancestor(root)

    def lowestCommonAncestor(self, root, p, q):
        if p.val > q.val:
            p, q = q, p
        while p.val != root.val and q.val != root.val:
            if p.val <= root.val <= q.val:
                return root
            elif root.val > q.val:
                root = root.left
            else:
                root = root.right

        return root
