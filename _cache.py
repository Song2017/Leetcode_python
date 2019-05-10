class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        def NQueens(n, index, row):
            if n == index:
                res.append(generateBoard(list(row)))
                return
            for i in range(n):
                if not col[i] and not diag1[index + i] and not diag2[index - i
                                                                     + n - 1]:
                    row.append(i)
                    col[i] = 1
                    diag1[index + i] = 1
                    diag2[index - i + n - 1] = 1
                    NQueens(n, index + 1, row)
                    col[i] = 0
                    diag1[index + i] = 0
                    diag2[index - i + n - 1] = 0
                    row.pop()

        def generateBoard(row):
            board = ['.' * n] * n
            for i in range(n):
                board[i] = board[i][:row[i]] + 'Q' + board[i][row[i] + 1:]
            return board

        col = [0 for i in range(n)]
        diag1 = [0 for i in range(2 * n - 1)]
        diag2 = [0 for i in range(2 * n - 1)]
        res = []
        NQueens(n, 0, [])
        return res
