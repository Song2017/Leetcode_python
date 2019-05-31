class Solution:
    def solveNQueens(self, n: int):
        '''
        n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
        二维矩阵存储棋盘状态, 采用递归解法
        '''

        def dfs(row, board, ret, size):
            # print(board, size, row)
            if row == size:
                ret.append(["".join(i) for i in board])
                return
            # 对每一列进行尝试
            for i in range(size):
                if not canPlace(row, i, board, size):
                    continue
                board[row][i] = 'Q'
                # 对每一行进行尝试, 同时也是回溯点
                dfs(row + 1, board, ret, size)
                # !! 将棋盘恢复为未摆放的状态
                board[row][i] = '.'

        def canPlace(row, col, board, size):
            # 只要对判断行之上的行进行判断, 当前判断行将要放置, 也不需要判断
            for i in range(1, row + 1):
                # 同一列
                if board[row - i][col] == 'Q':
                    return False
                # 上半对角线
                if col - i >= 0 and board[row - i][col - i] == 'Q':
                    return False
                # 上半逆对角线
                if col + i < size and board[row - i][col + i] == 'Q':
                    return False

            return True

        board, ret = [['.'] * n for _ in range(n)], []
        dfs(0, board, ret, n)
        return ret

    def solveNQueensOneDim(self, n: int):
        '''
        一维矩阵存储棋盘状态, 采用递归解法
        判断是否可以放置的条件:
            1, 判断列, 2, 判断两斜线: 行和列到将要放置点的距离相等的点是否已被放置
        '''
        memo, ret = [0] * n, []

        def canPlace(row, col):
            for i in range(0, row):
                if memo[i] == col or abs(col - memo[i]) == abs(row - i):
                    return False
            return True

        def dfs(row):
            if row == n:
                graph = []
                for i in memo:
                    graph.append('.' * i + 'Q' + '.' * (n - i - 1))
                ret.append(graph)
                return
            for i in range(n):
                if not canPlace(row, i):
                    continue
                memo[row] = i
                dfs(row + 1)
                memo[row] = 0

        dfs(0)
        return ret

    def solveNQueensRe(self, n: int):
        '''
        一维矩阵存储棋盘状态, 采用迭代
        '''
        memo, row, ret, graph = [0] * (n + 1), 1, [], []

        def canPlace(col):
            for i in range(1, col):
                # 判断列, 判断两斜线: 行和列到当前点的距离相等的位置
                if memo[i] == memo[col] or abs(memo[col] -
                                               memo[i]) == abs(col - i):
                    return False
            return True

        # 从第1行开始, 索引为0的行作为退出条件
        while row > 0:
            memo[row] += 1
            # 当前行放置, 不能放则
            while memo[row] <= n and not canPlace(row):
                memo[row] += 1
            if memo[row] <= n:
                # 已经放到最后一行了
                if row == n:
                    graph = []
                    for i in memo[1:]:
                        graph.append('.' * (i - 1) + 'Q' + '.' * (n - i))
                    ret.append(graph)
                else:
                    # 判断下一行
                    row += 1
                    # 下一行从第0列开始判断
                    memo[row] = 0
            else:
                row -= 1
        return ret


s = Solution()
print(s.solveNQueensRe(11))
