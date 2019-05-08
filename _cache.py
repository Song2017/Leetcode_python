class Solution(object):
    def solveNQueens(self, n):
        board, ret = [['.'] * n for _ in range(n)], []
        self.dfs(board, n, 0, ret)
        return ret

    def dfs(self, board, n, row, ret):
        print(ret)
        if row == n:
            ret.append(["".join(i) for i in board])
            return
        for i in range(n):
            if not self.canPlace(row, i, n, board):
                continue
            board[row][i] = 'Q'
            self.dfs(board, n, row + 1, ret)
            board[row][i] = '.'

    def canPlace(self, row, col, n, board):
        for i in range(1, row + 1):
            # 判断同一列上是否有Q
            if board[row - i][col] == 'Q':
                return False
            # 判断上半逆对角线是否有Q
            if col - i >= 0 and board[row - i][col - i] == 'Q':
                return False
            # 判断上半对角线是否有Q
            if col + i < n and board[row - i][col + i] == 'Q':
                return False
        return True


s = Solution()
print(s.solveNQueens(4))
