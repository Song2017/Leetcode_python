class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBoomerang(self, points) -> bool:
        '''
        回旋镖定义为一组三个点，这些点各不相同且不在一条直线上。
        给出平面上三个点组成的列表，判断这些点是否可以构成回旋镖。
        '''

        x, y, s = set(), set(), set()

        ans = list(set([tuple(p) for p in points]))

        if len(ans) != len(points):
            return False

        # print(ans)
        for p in points:
            # print(p, p[0])
            x.add(p[0])
            y.add(p[1])
            if p[1] == 0:
                s.add(-1)
            else:
                s.add(p[0]/p[1])
        if len(x) >= 2 and len(y) >= 2 and len(s) >= 2:
            return True

        return False

    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root is None:
            return []
        ans = root
        ary = self.inorderTraversal(root)
        
        ary = ary[::-1]
        # print(ary)
        for i, v in enumerate(ary):
            if i == 0: 
                continue
            # print(i,v)
            ary[i] = ary[i-1] + v
        ary = ary[::-1]            
 
        res, stack = [], []
        while stack or root:
            if root:
                stack.append(root) 
                root = root.right
            else:
                root = stack.pop()
                res.append(root)
                root = root.left
        print([r.val for r in res])
        res = res[::-1]
        while res:
            n = res.pop()
            n.val = ary.pop()
        return ans
    def inorderTraversal(self, root: TreeNode):
        rtn, stack = [], []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                rtn.append(root.val)
                root = root.right
        return rtn

s = Solution()
print(s.isBoomerang([[0, 0], [0, 0], [2, 1]]))
