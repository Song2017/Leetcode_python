from typing import List
from functools import lru_cache


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = 0
        stack = []
        for c in s:
            if not stack:
                ans += 1
                stack.append(c)
            else:
                if stack[-1] == c:
                    stack.append(c)
                else:
                    stack.pop()
        return ans

    def queensAttacktheKing(self, queens, king: List[int]):
        ans = []
        steps = 8 - min(king)
        ds = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
        for s in range(1, 8):
            cds = [[d[0] * s, d[1] * s] for d in ds]
            for i, j in cds:
                x, y = i + king[0], j + king[1]
                if 0 <= x <= 7 and 0 <= y <= 7 and [x, y] in queens:
                    ans.append([x, y])
                    ds.remove([i / s, j / s])
        ans.sort()
        return ans

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        """
        n的数字大于100, 不适用直接计算, 反向计算溢出
        正向计算
        """
        const_mod = int(1e9 + 7)

        @lru_cache(None)
        def dp(rolls, cur, repeats):
            if rolls == 0:
                return 1
            ans = 0
            for num in range(6):
                if num != cur:
                    ans += dp(rolls - 1, num, 1)
                elif repeats + 1 <= rollMax[num]:
                    ans += dp(rolls - 1, num, repeats + 1)
            ans %= const_mod
            return ans

        return dp(n, -1, 0) % const_mod

    def dieSimulatorTrue(self, n, rollMax):
        MOD = 10 ** 9 + 7

        @lru_cache(None)
        def dp(i, j, k):
            # i rolls, recently rolled j, k times
            if i == 0:
                return 1
            ans = 0
            for d in range(6):
                if d != j:
                    ans += dp(i - 1, d, 1)
                elif k + 1 <= rollMax[d]:
                    ans += dp(i - 1, d, k + 1)
            ans %= MOD
            return ans

        return dp(n, -1, 0) % MOD


if __name__ == "__main__":
    s = Solution()
    # print(s.balancedStringSplit("RLLLLRRRLR"))
    # print(
    #     s.queensAttacktheKing([[5, 6], [7, 7], [2, 1], [0, 7], [1, 6], [5, 1]], [3, 4])
    # )
    print(s.dieSimulator(20, [8, 5, 10, 8, 7, 2]))
    # print(s.dieSimulator(2, [1, 1, 1, 1, 1, 1]))

