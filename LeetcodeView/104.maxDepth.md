# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    dep = 0

    def maxDepth0(self, root: TreeNode) -> int:
        if not root:
            return self.dep
        root.val = 1

        def updateDep(root):
            if root is None:
                return 0
            if root.left:
                root.left.val = root.val + 1
            if root.right:
                root.right.val = root.val + 1
            self.dep = max(root.val, self.dep)
            updateDep(root.left)
            updateDep(root.right)

        updateDep(root)
        return self.dep

    def maxDepthQue(self, root):
        if root is None:
            return 0

        que, end, dep = [root], root, 0
        while que:
            # 弹出首元素
            pop = que.pop(0)
            # 添加一层的节点
            if pop.left:
                que.append(pop.left)
            if pop.right:
                que.append(pop.right)
            # 一层的节点已经遍历完
            if end == pop:
                dep += 1
                if que:
                    # 更新end, 一层的最左侧节点
                    end = que[-1]
        return dep

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not (root.right or root.left):
            return 1
        return max(self.maxDepth(root.right), self.maxDepth(root.left)) + 1
