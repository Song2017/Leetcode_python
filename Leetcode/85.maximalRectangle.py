class Solution:
    '''
    给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
    示例:
    输入:
    [
    ["1","0","1","0","0"],
    ["1","1","1","1","1"],
    ["1","0","1","1","1"],
    ["1","0","0","1","0"]
    ]
    输出: 6
    '''

    def rowMaxArea(self, dp):
        ans = 0
        stack = []
        dp = [0] + dp + [0]
        for i in range(len(dp)):
            while stack and dp[stack[-1]] > dp[i]:
                tmp = stack.pop()
                ans = max(ans, (i - stack[-1] - 1) * dp[tmp])
            stack.append(i)
        return ans

    def maximalRectangle(self, matrix) -> int:
        '''
        转化为求最大矩形面积
        '''
        n = len(matrix)
        if n == 0:
            return 0
        ans = 0
        heights = [0] * len(matrix[0])
        for r in range(n):
            for c in range(len(matrix[0])):
                heights[c] = heights[c] + 1 if matrix[r][c] == '1' else 0
            ans = max(ans, self.rowMaxArea(heights))
            # print(r, heights, matrix[r])

        return ans

    def maximalRectangle2(self, matrix) -> int:
        '''
        转化为求最大矩形面积
        高 * (行右可拓展最小 - 行左边可拓展最大)
        '''
        # 行数
        n = len(matrix)
        if n == 0:
            return 0
        ans = 0
        # 列数
        m = len(matrix[0])
        heights = [0] * m
        lefts = [0] * m
        rights = [m] * m
        for r in range(n):
            lcur, rcur = 0, m
            # heights
            for c in range(m):
                if matrix[r][c] == '1':
                    heights[c] += 1
                else:
                    heights[c] = 0
            # left
            for c in range(m):
                if matrix[r][c] == '1':
                    lefts[c] = max(lefts[c], lcur)
                else:
                    lefts[c] = 0
                    lcur = c + 1
            # right
            for c in range(m - 1, -1, -1):
                if matrix[r][c] == '1':
                    rights[c] = min(rights[c], rcur)
                else:
                    rights[c] = m
                    rcur = c
            # print(heights, lefts, rights)
            for c in range(m):
                ans = max(ans, (rights[c] - lefts[c]) * heights[c])
        return ans


if __name__ == "__main__":
    s = Solution()
    print(
        s.maximalRectangle2([["1", "0", "1", "0", "0"],
                             ["1", "0", "1", "1", "1"],
                             ["1", "1", "1", "1", "1"],
                             ["1", "0", "0", "1", "0"]]))
