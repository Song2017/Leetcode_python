class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        r1, r2, r3 = [], '', []
        for v in S:
            if v == '(' and len(r1) == 0:
                r1.append('(')
            else:
                if v == '(':
                    r3.append('(')
                    r2 += v
                else:
                    if len(r3) > 0:
                        r3.pop()
                        r2 += v
                    else:
                        r1.pop()
        return r2

    def sumRootToLeaf(self, root: TreeNode) -> int:
        if None == root:
            return 0
        return self.sumRTL(root, 0) % 1000000007

    def sumRTL(self, root, s):
        if None == root:
            return 0
        else:
            s = (s * 2 + root.val)
            if root.left is None and root.right is None:
                return s
            else:
                return self.sumRTL(root.left, s) + self.sumRTL(root.right, s)
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        nums = len(pattern)
        rtn = [True]*len(queries)
        for i, q in enumerate(queries):
            pos = 0
            for c in q:
                if pos < nums and c == pattern[pos]:
                    pos += 1
                else:
                    if  'A'<= c and c <= 'Z':
                        rtn[i] = False
                        break
            if pos < nums:
                rtn[i] = False
        return rtn

    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        for t in range(T):
            tmp = t
            for clip in clips:
                if t in clip:
                    tmp += 1
            if tmp == t:
                return -1


s = Solution()
# print(s.removeOuterParentheses('(()())(())(()(()))'))
print(s.removeOuterParentheses("(())"))
print(s.removeOuterParentheses("((()())(()()))"))
