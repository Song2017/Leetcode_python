# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        '''
        记录每个节点的最大路径值,
        返回节点所在最大路径值时, 1: 只能选取一侧的值; 2: 小于0的值不进行选择
        '''
        if root.left is None and root.right is None:
            return root.val
        self.ans = []

        def pathSum(node):
            if node is None:
                return 0
            self.ans.append(node.val)
            if node.left is None and node.right is None:
                return node.val
            lv = pathSum(node.left)
            rv = pathSum(node.right)
            v = node.val + max(max(rv, lv), 0)
            self.ans.append(max(v, v + min(rv, lv)))
            return max(v, 0)

        pathSum(root)

        return max(self.ans)

    def maxPathSumF(self, root) -> int:
        def pathSum(node):
            if node is None:
                return 0
            lv = pathSum(node.left)
            rv = pathSum(node.right)
            self.ans = max(node.val + lv + rv, self.ans)
            return max(node.val + max(rv, lv), 0)
        self.ans = float('-inf')
        pathSum(root)
        return self.ans


n = TreeNode(1)
n1 = TreeNode(-2)
n2 = TreeNode(3)
n.left = n1
n.right = n2

# [5,4,8,11,null,13,4,7,2,null,null,null,1] [-10,9,20,null,null,15,7] [9,6,-3,null,null,-6,2,null,null,2,null,-6,-6,-6]
s = Solution()
print(s.maxPathSum(n))