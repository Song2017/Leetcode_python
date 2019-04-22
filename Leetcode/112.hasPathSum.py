# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    '''
    给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，
    这条路径上所有节点值相加等于目标和

    左右子节点取并集, 
    这时递归终止条件就变成: 节点不存在取假, 子节点均不存在时判断值是否相等
    '''

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        self.sum_val = sum

        def sumPath(root, s):
            if root.left and root.right:
                return sumPath(root.left, s + root.left.val) or\
                    sumPath(root.right, s + root.right.val)
            elif root.left:
                return sumPath(root.left, s + root.left.val)
            elif root.right:
                return sumPath(root.right, s + root.right.val)
            else:
                if s == self.sum_val:
                    return True
                else:
                    return False

        return sumPath(root, root.val)

    def hasPathSumReduce(self, root: TreeNode, s: int) -> bool:
        if root is None:
            return False
        s -= root.val
        if root.left is None and root.right is None:
            return s == 0

        return self.hasPathSumReduce(root.left, s) or self.hasPathSumReduce(
            root.right, s)
