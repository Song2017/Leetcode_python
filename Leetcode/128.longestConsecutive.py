from typing import List


class Solution:
    '''
    给定一个未排序的整数数组，找出最长连续序列的长度。
    要求算法的时间复杂度为 O(n)。
    示例:
    输入: [100, 4, 200, 1, 3, 2]
    输出: 4
    解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4
    '''

    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        根据要求时间复杂度为O(n), 想到集合和哈希表
        计算长度, 考虑到线性空间和数字累加
        '''
        if not nums:
            return 0
        s = set(nums)
        ans = 0
        for n in s:
            # 寻找连续序列的最小值
            if n - 1 in s:
                continue
            cur = n + 1
            cnt = 1
            # while 循环在整个运行过程中只会被迭代 n 次
            while cur in s:
                cnt += 1
                cur += 1
            ans = max(ans, cnt)
        return ans
