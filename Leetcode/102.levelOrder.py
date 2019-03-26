# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder0(self, root: TreeNode):
        if root is None:
            return []
        rtn, level, odd, even = [], [], [], []
        odd.append(root)
        isodd = True
        while odd or even:
            if isodd:
                tmp = odd.pop()
                level.append(tmp.val)
                if tmp.left:
                    even.append(tmp.left)
                if tmp.right:
                    even.append(tmp.right)
                if len(odd) == 0:
                    even.reverse()
                    rtn.append(level)
                    level = []
                    isodd = False
            else:
                tmp = even.pop()
                level.append(tmp.val)
                if tmp.left:
                    odd.append(tmp.left)
                if tmp.right:
                    odd.append(tmp.right)
                if len(even) == 0:
                    odd.reverse()
                    rtn.append(level)
                    level = []
                    isodd = True
        return rtn

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q = [root]
        res = []
        while q:
            tmp = []
            q2 = []
            for i in q:
                tmp.append(i.val)
                if i.left:
                    q2.append(i.left)
                if i.right:
                    q2.append(i.right)
            res.append(tmp)
            q = q2
        return res
