class Solution:
    '''
    给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
    '''

    def trap_row_TLE(self, height) -> int:
        '''
        从底部向上, 一层一层来
        '''
        n = len(height)
        if n == 0:
            return 0
        ans = 0

        for h in range(1, max(height) + 1):
            temp = 0
            isStart = False
            for v in height:
                if isStart and v < h:
                    temp += 1
                if v >= h:
                    ans += temp
                    temp = 0
                    isStart = True

        return ans

    def trap_col(self, height) -> int:
        '''
        分开来看每一列, 当前列能存住的雨滴: 两侧列中较低的与当前列高度的差值
        时间复杂度：O(n²），遍历每一列需要 n，
            找出左边最高和右边最高的墙加起来刚好又是一个 n，所以是 n²
        空间复杂度：O(1）
        '''
        n = len(height)
        ans = 0
        for i in range(1, n):

            ml = max(height[:i])
            mr = max(height[i:])

            tmp = min(ml, mr)
            if height[i] < tmp:
                ans += tmp - height[i]
        return ans

    def trap_dp(self, height) -> int:
        '''
        分开来看每一列, 当前列能存住的雨滴: 两侧列中较低的与当前列高度的差值
        空间换时间, 数组暂存左右最大值
        时间复杂度：O(n），遍历每一列需要 n
        空间复杂度：O(n）
        '''
        n = len(height)
        ans = 0
        if n == 0:
            return ans
        ml = [0] * n
        mr = [0] * n

        tmp = height[0]
        for i in range(1, n - 1):
            tmp = max(tmp, height[i])
            ml[i] = tmp
        tmp = height[-1]
        for i in range(n - 2, 0, -1):
            tmp = max(tmp, height[i])
            mr[i] = tmp

        for i in range(1, n):
            tmp = min(ml[i], mr[i])
            if height[i] < tmp:
                ans += tmp - height[i]
        return ans

    def trap_dbp(self, height) -> int:
        '''
        分开来看每一列, 当前列能存住的雨滴: 两侧列中较低的与当前列高度的差值
        双指针: 两侧的最大值跟紧邻的外侧列相关
        能存住的水滴取决于两侧中低的一侧, 从两侧逼近时只要关心紧邻的外侧列中低的一列
        时间复杂度：O(n）
        空间复杂度：O(1）
        '''
        n = len(height)
        ans = 0
        left, right, ml, mr = 1, n - 2, 0, 0
        while left <= right:
            # 从左向右
            if height[left - 1] < height[right + 1]:
                ml = max(height[left - 1], ml)
                if (height[left] < ml):
                    ans += ml - height[left]
                left += 1
            else:
                mr = max(height[right + 1], mr)
                if (height[right] < mr):
                    ans += mr - height[right]
                right -= 1
        return ans


if __name__ == "__main__":
    Solution1 = Solution()
    print(Solution1.trap_dbp([1, 0, 1]))
