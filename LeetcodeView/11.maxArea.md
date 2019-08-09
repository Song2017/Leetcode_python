class Solution:
    def maxArea(self, height) -> int:
        '''
        给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
        在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
        找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水
        '''
        ma, li, r = 0, 0, len(height) - 1
        while li < r:
            h, w, lv, rv = r - li, 0, height[li], height[r]
            # print(li, h, lv, rv)
            if lv > rv:
                r -= 1
                w = rv
            else:
                li += 1
                w = lv
            if ma < w * h:
                ma = w * h

        return ma


s = Solution()
print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
