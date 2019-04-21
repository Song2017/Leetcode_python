# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        '''
        给定一个二叉树，判断其是否是一个有效的二叉搜索树。
        假设一个二叉搜索树具有如下特征：
            节点的左子树只包含小于当前节点的数。
            节点的右子树只包含大于当前节点的数。
            所有左子树和右子树自身必须也是二叉搜索树。

        中序遍历为严格升序
        '''
        if root is None:
            return False
        if root.right is None and root.left is None:
            return True
        inOrder, stack = [], []

        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                inOrder.append(root.val)
                root = root.right

        for i, v in enumerate(inOrder):
            if i == 0:
                continue
            if v < inOrder[i-1]:
                return False

        return True
