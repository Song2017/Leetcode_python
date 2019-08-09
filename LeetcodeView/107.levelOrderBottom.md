# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    '''
    给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
    '''
    def levelOrderBottom(self, root: TreeNode):
        if not root:
            return []
        # q: 队列存储每层的节点
        ans, q = [], [root]
        while q:
            level, qt = [], []
            for n in q:
                level.append(n.val)
                # qt: 下一层节点的缓存, 要保持层内节点的顺序, 需要先添加左侧子节点
                if n.left:
                    qt.append(n.left)
                if n.right:
                    qt.append(n.right)
            q = qt
            ans.append(level)
        ans.reverse()
        return ans
