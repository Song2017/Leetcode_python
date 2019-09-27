class Solution:
    '''给定一个无序的整数数组，找到其中最长上升子序列的长度。

        示例:

        输入: [10,9,2,5,3,7,101,18]
        输出: 4
        解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
        说明:

        可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
        你算法的时间复杂度应该为 O(n2)
    '''

    def lengthOfLIS(self, nums) -> int:
        '''子序列的问题->动态规划。
        使用数组 d 保存每步子问题的最优解。d[i] 代表含第 i 个元素的最长上升子序列的长度。
        因为已知d[0],...d[i-1]无法推导出d[i], 所以转换思路, 改为在d[0],...d[i-1]后追加nums[i], 逐个求解
        求解 d[i] 时，向前遍历找出比 i 元素小的元素 j，令 d[i] 为 max（cell[i],d[j]+1)。
        '''
        n = len(nums)
        if n <= 1:
            return n
        d = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    d[i] = max(d[j] + 1, d[i])
        return max(d)

    def lengthOfLIS_Stack(self, nums) -> int:
        '''
        cell，用于保存最长上升子序列。
        对原序列进行遍历，将每位元素二分插入 cell 中。
        如果 cell 中元素都比它小，将它插到最后
        否则，用它覆盖掉比它大的元素中最小的那个。
        总之，思想就是让 cell 中存储比较小的元素。这样，cell 未必是真实的最长上升子序列，但长度是对的
        '''
        n = len(nums)
        if n <= 1:
            return n

        ans = [nums[0]]
        for num in nums[1:]:
            if num > ans[-1]:
                ans.append(num)
                continue

            l, r = 0, len(ans) - 1
            while l < r:
                middle = l + (r - l) // 2
                if num > ans[middle]:
                    l = middle + 1
                else:
                    r = middle
            ans[l] = num

        return len(ans)
