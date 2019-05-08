class Solution:
    def solveNQueens(self, n: int):
        '''
        n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
        '''
        memo = [['.'] * n for _ in range(n)]

        return memo


s = Solution()
print(s.solveNQueens(3))