class Solution:
    '''
    给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
    输入:[[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]]
    输出: [1,2,3,6,9,8,7,4,5]        
    '''

    def spiralOrder(self, matrix):
        '''
        判断行是否全部遍历, 根据isHorizon判断读取水平还是竖直, 根据已遍历行数判断读取的方向
        '''
        if matrix == []:
            return []
        row, col, cntR, isHorizon, ans = len(matrix), \
            len(matrix[0]), 0, True, []
        while cntR < row:
            if len(ans) == row * col:
                break
            intervalR = cntR >> 1
            if isHorizon:
                if cntR % 2 == 0:
                    for i in range(intervalR, col - intervalR):
                        ans.append(matrix[intervalR][i])
                else:
                    for i in range(col - 2 - intervalR, intervalR - 1, -1):
                        ans.append(matrix[row - 1 - intervalR][i])
                cntR += 1
            else:
                if cntR % 2 == 1:
                    for i in range(intervalR + 1, row - intervalR):
                        ans.append(matrix[i][col - 1 - intervalR])
                else:
                    for i in range(row - 1 - intervalR, intervalR - 1, -1):
                        ans.append(matrix[i][intervalR - 1])
            isHorizon = not isHorizon
        return ans

    def spiralOrder2(self, matrix):
        '''
        根据isHorizon判断读取水平还是竖直, 根据已遍历行数判断读取的方向
        根据结果数组中元素个数判断是否继续遍历
        '''
        if matrix == []:
            return []
        row, col, cntR, isHorizon, ans = len(matrix), \
            len(matrix[0]), 0, True, []
        while len(ans) < row * col:
            intervalR = cntR >> 1
            if isHorizon:
                if cntR % 2 == 0:
                    for i in range(intervalR, col - intervalR):
                        ans.append(matrix[intervalR][i])
                else:
                    for i in range(col - 2 - intervalR, intervalR - 1, -1):
                        ans.append(matrix[row - 1 - intervalR][i])
                cntR += 1
            else:
                if cntR % 2 == 1:
                    for i in range(intervalR + 1, row - intervalR):
                        ans.append(matrix[i][col - 1 - intervalR])
                else:
                    for i in range(row - 1 - intervalR, intervalR - 1, -1):
                        ans.append(matrix[i][intervalR - 1])
            isHorizon = not isHorizon
        return ans

    def spiralOrderF(self, matrix):
        '''
        参考大牛写的, 判断何时转向的思想很巧妙
        1, 有两个方向, 所以使用二维元组存储方向状态
            上右:(0, 1), 右下(1, 0), 下左(0, -1), 左上(-1, 0)
        2, 判断如何转向
            读取数据时, 每行,列的最后一个元素是将要读取的列,行的起点.
            起点已经被读取, 就想到取模操作可以得到当前列,行的下一步状态.
        '''
        if matrix == []:
            return []
        i, j, di, dj, m, n, ans = 0, 0, 0, 1, len(matrix), len(matrix[0]), []
        for _ in range(m * n):
            ans.append(matrix[i][j])
            matrix[i][j] = None
            if matrix[(i + di) % m][(j + dj) % n] is None:
                di, dj = dj, -di
            i, j = i + di, j + dj
            # print(i, j, di, dj)
        return ans


s = Solution()
print(s.spiralOrderF([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
# print(s.spiralOrderF([[1], [2], [3], [4]]))
