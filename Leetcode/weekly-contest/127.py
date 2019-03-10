class Solution:
    def largestSumAfterKNegations(self, A, K):
        '''
        K 次取反后最大化的数组和
        输入：A = [2,-3,-1,5,-4], K = 2
        输出：13
        解释：选择索引 (1, 4) ，然后 A 变为 [2,3,-1,5,4]        
        '''
        aryLess = []
        rtn = 0
        for i in A:
            if i < 0:
                aryLess.append(i)
            else:
                rtn += i
        lenLess = len(aryLess)
        if lenLess == 0:
            return rtn - 2 * min(A)
        aryLess.sort()
        if lenLess >= K:
            rtn = rtn - sum(aryLess[:K]) + sum(aryLess[K:])
        elif 0 in A:
            rtn = rtn - sum(aryLess[:lenLess])
        else:
            rtn = rtn - sum(aryLess[:lenLess])
            if (K - lenLess) % 2 == 1:
                AP = [abs(i) for i in A]
                rtn = sum(AP) - 2 * min(AP)
        return rtn

    def largestSumAfterKNegationsF(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        heapq.heapify(A)
        for i in range(K):
            p = heapq.heappop(A)
            if p == 0:
                break
            heapq.heappush(A, -p)
        return sum(A)

    def clumsy(self, N):
        '''
        clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1
        '''
        cnt = -1
        rtn = [N]
        for i in range(N - 1, 0, -1):
            cnt += 1
            print(rtn, cnt)
            if cnt == 4:
                cnt = 0
            if cnt == 0:
                rtn.append(rtn.pop() * i)
            elif cnt == 1:
                rtn.append(int(rtn.pop() / i))
            elif cnt == 2:
                rtn.append(i)
            else:
                rtn.append(-i)
        return sum(rtn)

    def clumsyF(self, N):
        """
        :type N: int
        :rtype: int
        """
        s = []
        o = ['*', '//', '+', '-']
        k = 0
        for i in range(N, 0, -1):
            s.append(str(i))
            s.append(o[k])
            k = (k + 1) % 4
        s.pop()
        return eval(''.join(s))

    def minDominoRotationsF(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """

        n = len(A)
        a = collections.Counter(A)
        b = collections.Counter(B)
        c = a + b
        m = c.most_common(1)[0]
        if m[1] < n:
            return -1
        cand = m[0]
        ac, bc = 0, 0
        for i in range(n):
            if cand != A[i]:
                if cand != B[i]:
                    return -1
                ac += 1
            elif cand != B[i]:
                bc += 1
        return min(ac, bc)

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    def bstFromPreorderF(self, p):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        if not p:
            return None
        ret = TreeNode(p[0])
        i = 1
        while i < len(p) and p[i] < p[0]:
            i += 1
        ret.left = self.bstFromPreorder(p[1:i])
        ret.right = self.bstFromPreorder(p[i:])
        return ret


s = Solution()
print(s.clumsy(10))
print(s.clumsy(4))

print(s.largestSumAfterKNegations([4, 2, 3], 1))
print(s.largestSumAfterKNegations([3, -1, 0, 2], 3))
print(s.largestSumAfterKNegations([2, -3, -1, 5, -4], 2))
print(s.largestSumAfterKNegations([5, 6, 9, -3, 3], 2))
