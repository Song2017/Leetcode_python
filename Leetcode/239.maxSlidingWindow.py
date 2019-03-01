class Solution:
    def maxSlidingWindow0(self, nums, k: int):
        '''
        给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
        你只可以看到在滑动窗口 k 内的数字。滑动窗口每次只向右移动一位。
        返回滑动窗口最大值。
        输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
        输出: [3,3,5,5,6,7]
        '''
        if len(nums) <= 0:
            return []

        maxAry = [None] * (len(nums) - k + 1)

        for i in range(len(maxAry)):
            maxAry[i] = max(nums[i:i + k])

        return maxAry

    def maxSlidingWindow(self, nums, k: int):
        '''
        给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
        你只可以看到在滑动窗口 k 内的数字。滑动窗口每次只向右移动一位。
        返回滑动窗口最大值。
        输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
        输出: [3,3,5,5,6,7]
        '''
        if len(nums) <= 0:
            return nums
        max_ary = [max(nums[:k])]
        max_val = max_ary[0]
        for i in range(k, len(nums)):
            if nums[i] > max_val:
                max_val = nums[i]
            # 最大值滑出窗口
            elif nums[i - k] == max_val:
                max_val = max(nums[i - k + 1:i + 1])
            max_ary.append(max_val)
        return max_ary


s = Solution()
print(s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
print(s.maxSlidingWindow([1, -1], 1))
print(s.maxSlidingWindow([7, 2, 4], 2))
