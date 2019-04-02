# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def deleteNodeBST(self, root: TreeNode, p: TreeNode, key: int):
        if key < root.val:
            if not root.left:
                return root
            self.deleteNodeBST(root.left, root, key)
        elif key > root.val:
            if not root.right:
                return root
            self.deleteNodeBST(root.right, root, key)
        else:
            # 找到这个节点的右子树中的最小节点，把它替换到要删除的节点上,然后再删除掉这个最小节点
            if root.left and root.right:
                minnodep = root
                minnode = root.right
                while minnode.left:
                    minnodep = minnode
                    minnode = minnode.left
                root.val = minnode.val
                if root.right.val == minnode.val:
                    root.right = root.right.right
                else:
                    minnodep.left = None
            else:
                # 当前节点与其父节点的关系
                if root.val > p.val:
                    if root.right:
                        p.right = root.right
                    elif root.left:
                        p.right = root.left
                    else:
                        p.right = None
                else:
                    if root.right:
                        p.left = root.right
                    elif root.left:
                        p.left = root.left
                    else:
                        p.left = None

        return root

    def deleteNodeE(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return None

        self.deleteNodeBST(root, root, key)

        return root

    def min(self, root):
        while root.left:
            root = root.left
        return root

    def removeMin(self, root):
        '''
        去掉最小节点后, 返回根节点
        [2,0,33,null,1,25,40,null,null,11,31,34,45,10,18,29,32,null,36,43,46,4,null,12,24,26,30,null,null,35,39,42,44,null,48,3,9,null,14,22,null,null,27,null,null,null,null,38,null,41,null,null,null,47,49,null,null,5,null,13,15,21,23,null,28,37,null,null,null,null,null,null,null,null,8,null,null,null,17,19,null,null,null,null,null,null,null,7,null,16,null,null,20,6]
        33       
        '''
        # rn = root
        # min_p = root
        # while root:
        #     if not root.left:
        #         right = root.right
        #         root.right = None
        #         return right
        #     min_p = root
        #     root = root.left
        # min_p.left = None
        # return rn
        if not root.left:
            right = root.right
            root.right = None
            return right
        root.left = self.removeMin(root.left)
        return root

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        else:
            # 单子节点为空, 只需处理另一个子节点
            if not root.right:
                left = root.left
                root.left = None
                return left
            if not root.right:
                right = root.right
                root.right = None
                return right
            else:
                # 均为空或均不为空
                # 取右子树中最小节点
                minr = self.min(root.right)
                # 去掉最小节点后的右子树根节点
                minr.right = self.removeMin(root.right)
                minr.left = root.left
                # 释放原来的root
                root.left = root.right = None
                return minr
