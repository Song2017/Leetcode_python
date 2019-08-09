class Solution:
    '''
    给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
    输入: 3
    输出:[[ 1, 2, 3 ],[ 8, 9, 4 ],[ 7, 6, 5 ]]    
    '''
    def generateMatrix(self, n):
        ans = [[0] * n for _ in range(n)]
        x, y, dx, dy = 0, 0, 0, 1
        for i in range(1, n * n + 1):
            ans[x][y] = i
            if ans[(x + dx) % n][(y + dy) % n] > 0:
                dx, dy = dy, -dx
            x, y = x + dx, y + dy
        return ans


s = Solution()
print(s.generateMatrix(3))
