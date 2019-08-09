# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        parent = None
        node = root
        while (node and node.val != key):
            parent = node
            if node.val > key:
                node = node.left
            else:
                node = node.right
        # not found
        if not node:
            return root
        # node does't has child
        elif not node.left and not node.right:
            # not root
            if parent:
                if parent.left == node:
                    parent.left = None
                else:
                    parent.right = None
                return root
            # root
            return None
        # node  has two children
        elif node.left and node.right:
            pre_parent = node
            pre = node.left
            while pre.right:
                pre_parent = pre
                pre = pre.right
            if pre_parent != node:
                pre_parent.right = pre.left
                node.val = pre.val
            else:
                node.val = pre.val
                node.left = pre.left
            return root

        # node only has one child
        else:
            if parent:
                if parent.left == node:
                    parent.left = node.left or node.right
                else:
                    parent.right = node.left or node.right
                return root
            else:
                return node.left or node.right

    def deleteNodeF(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """

        parent = None
        node = root
        while (node and node.val != key):
            parent = node
            if node.val > key:
                node = node.left
            else:
                node = node.right
        # not found
        if not node:
            return root
        # node does't has child
        elif not node.left and not node.right:
            # not root
            if parent:
                if parent.left == node:
                    parent.left = None
                else:
                    parent.right = None
                return root
            # root
            return None
        # node  has two children
        elif node.left and node.right:
            pre_parent = node
            pre = node.left
            while pre.right:
                pre_parent = pre
                pre = pre.right
            if pre_parent != node:
                pre_parent.right = pre.left
                node.val = pre.val
            else:
                node.val = pre.val
                node.left = pre.left
            return root

        # node only has one child
        else:
            if parent:
                if parent.left == node:
                    parent.left = node.left or node.right
                else:
                    parent.right = node.left or node.right
                return root
            else:
                return node.left or node.right

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
            if not root.left:
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
