class Solution:
    '''给定一个未经排序的整数数组，找到最长且连续的的递增序列。
        示例 1:
        输入: [1,3,5,4,7]
        输出: 3
        解释: 最长连续递增序列是 [1,3,5], 长度为3。
        尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为5和7在原数组里被4隔开。
    '''

    def findLengthOfLCIS_Easy(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0
        ans = [1] * len(nums)
        for k in range(len(nums)):
            sub = [nums[k]]
            for i in nums[k + 1:]:
                if i <= sub[-1]:
                    break
                sub.append(i)
                ans[k] += 1
        return max(ans)

    def findLengthOfLCIS_O_n(self, nums) -> int:
        '''
        从 0 位置开始遍历，遍历时根据前后元素状态判断是否递增，
            递增则 count++，递减则 count=1
            对比当前元素与前一元素
        '''
        if nums is None or len(nums) <= 1:
            return len(nums)
        ans = 1
        count = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                count = count + 1
            else:
                count = 1
            if count > ans:
                ans = count

        return ans
