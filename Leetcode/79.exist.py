class Solution:
    def exist(self, board, word: str) -> bool:
        '''
        给定一个二维网格和一个单词，找出该单词是否存在于网格中。
        单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
        同一个单元格内的字母不允许被重复使用。
        board =[['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']]
        给定 word = "ABCCED", 返回 true.
        给定 word = "SEE", 返回 true.
        给定 word = "ABCB", 返回 false.

        简单版的八皇后
        回溯思想: 深度遍历 + 递归实现
        '''
        if len(word) == 0:
            return True

        r, c = len(board), len(board[0])
        states = [[0] * c for _ in range(r)]

        def dfs(word, states, x, y):
            print(word, x, y)
            if len(word) == 0:
                return True
            for ix, iy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                nx, ny = x + ix, y + iy
                if (-1 < nx < r) and (-1 < ny < c) and (
                        board[nx][ny] == word[0]) and (states[nx][ny] == 0):
                    states[nx][ny] = 1
                    if dfs(word[1:], states, nx, ny):
                        return True
                    states[nx][ny] = 0
            return False

        for i in range(r):
            for j in range(c):
                if board[i][j] == word[0] and states[i][j] == 0:
                    states[i][j] = 1
                    if dfs(word[1:], states, i, j):
                        return True
                    states[i][j] = 0

        return False


s = Solution()
print(
    s.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "ABCCED"))
