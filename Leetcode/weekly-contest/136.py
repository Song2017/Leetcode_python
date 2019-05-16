class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y, d = 0, 0, 0
        for _ in range(5):
            for inst in instructions:
                if inst == 'G':
                    if d == 0:
                        x += 1
                    elif d == 1:
                        y -= 1
                    elif d == 2:
                        x -= 1
                    else:
                        y += 1
                elif inst == 'length':
                    d = (d + 1) % 4
                elif inst == 'R':
                    d = d - 1 if d - 1 >= 0 else 3
                print(inst, x, y, d)
            if x == 0 and y == 0:
                return True
        return False

    def gardenNoAdj(self, N, paths):
        import collections
        edges = collections.defaultdict(list)
        for u, v in paths:
            edges[u - 1].append(v - 1)
            edges[v - 1].append(u - 1)
        res = [-1] * N
        for i in range(N):
            s = {1, 2, 3, 4}
            # 排除已经与其相连的花园中的花
            for j in edges[i]:
                s -= {
                    res[j],
                }
            res[i] = s.pop()
        return res

    def maxSumAfterPartitioning(self, A, K: int) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def dp(n):
            if n < 0:
                return 0
            if n == 0:
                return A[0]
            res = m = 0
            for i in range(n, max(-1, n - K), -1):
                m = max(m, A[i])
                res = max(res, (n - i + 1) * m + dp(i - 1))
            return res

        return dp(len(A) - 1)

    def maxSumAfterPartitioning2(self, A, K: int) -> int:
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        给出整数数组 A，将该数组分隔为长度最多为 K 的几个（连续）子数组。
        分隔完成后，每个子数组的中的值都会变为该子数组中的最大值。
        返回给定数组完成分隔后的最大和。
        t: 数组对应元素索引下最大的和
        """
        length = len(A)
        if length <= K:
            return max(A) * length
        if K == 1:
            return sum(A)
        t = [0] * length
        a = 0
        # 第一组最大的值
        for i in range(K):
            if A[i] > a:
                a = A[i]
            t[i] = a * (i + 1)
        # print(t)
        for i in range(K, length):
            a = 0
            for j in range(K):
                # 只要判断截止到当前元素的最大和,
                a = max(a, A[i - j])
                print(i, j, a, t)
                t[i] = max(t[i], a * (j + 1) + t[i - j - 1])
        return t[-1]


s = Solution()
# s.twoCitySchedCost([[10, 20], [30, 200], [400, 50], [30, 20]])
# print(s.isRobotBounded("GL"))
# print(s.gardenNoAdj(4, [[1, 2], [3, 4]]))
print(s.maxSumAfterPartitioning2([1, 17, 7, 9, 2, 5, 10], 3))
