class Solution:
    '''给定一个未排序的整数数组，找到最长递增子序列的个数。
    示例 1:
    输入: [1,3,5,4,7]
    输出: 2
    解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]
    求解 d[i] 时，向前遍历找出比 i 元素小的元素 j，令 d[i] 为 max（cell[i],d[j]+1)。
    求解 dc 时, 当前元素大于前一元素时要加上前一元素的长度, 若小于则取前一元素的长度
    '''

    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n

        m, d, dc = 0, [1] * n, [1] * n
        for cur in range(1, n):
            for pre in range(cur):
                if nums[cur] > nums[pre]:
                    if d[pre] + 1 > d[cur]:
                        d[cur] = d[pre] + 1
                        dc[cur] = dc[pre]
                    elif d[pre] + 1 == d[cur]:
                        # 发现了新的组合
                        dc[cur] += dc[pre]
        m = max(d)

        return sum([dc[i] for i in range(n) if d[i] == m])