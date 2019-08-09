# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    '''
    给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。
    说明：你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。
    '''

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # 中序遍历得到顺序数组
        stack, ans = [], [0]
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                ans.append(root.val)
                root = root.right
        return ans[k]

    def kthSmallestGen(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        # 中序遍历得到顺序数组
        def gen(root):
            print(root.val)
            if root:
                yield from gen(root.left)
                yield root.val
                yield from gen(root.right)

        it = gen(root)
        for _ in range(k):
            ans = next(it)

        return ans


s = Solution()
# print(s.kthSmallestGen())