class Solution:
    '''
    给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 
    求在该柱状图中，能够勾勒出来的矩形的最大面积
    '''

    def largestRectangleArea(self, heights) -> int:
        '''
        找两边第一个小于它的值

        la的值是左边第一个小于它的值的索引
        '''
        n = len(heights)
        if n == 0:
            return 0
        ans = 0
        la = [-1] * n
        ra = [n] * n
        # 左边
        for i in range(1, n):
            tmp = i - 1
            while tmp > -1 and heights[tmp] >= heights[i]:
                tmp = la[tmp]
            la[i] = tmp
        # 右边
        for i in range(n - 2, -1, -1):
            tmp = i + 1
            while tmp < n and heights[i] <= heights[tmp]:
                tmp = ra[tmp]
            ra[i] = tmp
        # print(la, ra)
        for i in range(n):
            ans = max(ans, heights[i] * (ra[i] - la[i] - 1))
        return ans

    def largestRectangleArea2(self, heights) -> int:
        '''
        维护一个递增栈
        '''
        stack = []
        heights = [0] + heights + [0]
        ans = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                ans = max(ans, (i - stack[-1] - 1) * heights[tmp])
            stack.append(i)
        return ans


if __name__ == "__main__":
    s = Solution()
    # print(s.largestRectangleArea2([2, 1, 2]))
    print(s.largestRectangleArea2([4, 2, 0, 3, 2, 4, 3, 4]))
