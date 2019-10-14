from typing import List


class Solution:
    '''
    给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，
    并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。
    '''

    def numIslands_dfs(self, grid) -> int:
        '''
        遍历岛屿, self.marks[i][j]标记已经查找过的网格
        深度优先, 回溯法
        '''
        rows = len(grid)
        if rows == 0:
            return 0

        cols = len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.marks = [[False] * cols for _ in range(rows)]
        ans = 0

        # 更新同一座岛屿的网格标识
        def dfs(i, j):
            self.marks[i][j] = True
            for d in dirs:
                x, y = d[0] + i, d[1] + j
                if 0 <= x < rows and 0 <= y < cols and not self.marks[x][
                        y] and grid[x][y] == '1':
                    dfs(x, y)

        for r in range(rows):
            for c in range(cols):
                if not self.marks[r][c] and grid[r][c] == '1':
                    ans += 1
                    dfs(r, c)
        return ans

    def numIslands_bfs(self, grid) -> int:
        '''
        广度优先, 数组存储单个岛屿所有的网格
        '''
        rows = len(grid)
        if rows == 0:
            return 0

        cols = len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        marks = [[False] * cols for _ in range(rows)]
        ans, bfs = 0, []

        for r in range(rows):
            for c in range(cols):
                if marks[r][c] or grid[r][c] == '0':
                    continue
                ans += 1
                marks[r][c] = True
                bfs.append((r, c))
                # 更新同一座岛屿的网格标识
                while bfs:
                    i, j = bfs.pop()
                    # 遍历同一个岛屿
                    for d in dirs:
                        x, y = d[0] + i, d[1] + j
                        if 0 <= x < rows and 0 <= y < cols and not marks[x][
                                y] and grid[x][y] == '1':
                            marks[x][y] = True
                            bfs.append((x, y))
        return ans

    def numIslands_ufa(self, grid) -> int:
        '''
        并查集 (union find algrithem): 树形结构的应用
        同一个岛屿的网格对应的根值是同一个
        '''
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        s = {}

        def find(x):
            s.setdefault(x, x)
            if s[x] != x:
                # 返回根键值
                s[x] = find(s[x])
            return s[x]

        def union(x, y):
            s[find(x)] = find(y)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != '1':
                    continue
                for (i, j) in [(-1, 0), (0, -1)]:
                    x, y = i + r, j + c
                    if 0 <= x < rows and 0 <= y < cols and grid[x][y] == '1':
                        union(x * cols + y, r * cols + c)
        print(s)
        ans = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    ans.add(find(r * cols + c))
        print(s)
        return ans


if __name__ == "__main__":
    s = Solution()
    # print(
    #     s.numIslands([["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"],
    #                   ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]))
    print(
        s.numIslands_ufa([["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"],
                          ["0", "0", "1", "0", "0"], ["0", "0", "0", "1",
                                                      "1"]]))
