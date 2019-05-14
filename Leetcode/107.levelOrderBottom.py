# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode):
        if not root:
            return []
        ans, q = [], [root]
        while q:
            level, qt = [], []
            for n in q:
                level.append(n.val)

                if n.left:
                    qt.append(n.left)
                if n.right:
                    qt.append(n.right)
            q = qt
            ans.append(level)
        ans.reverse()
        return ans
    