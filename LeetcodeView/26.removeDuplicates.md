class Solution:
    def removeDuplicates(self, nums) -> int:
        '''
        不需要删除, 只更新对应的数字到对应的位置
        ans: 不重复数字的索引
        '''
        n, ans = len(nums), 1
        if n < 2:
            return n
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                continue
            nums[ans] = nums[i]
            ans += 1
        return ans


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
s = Solution()

print(s.removeDuplicates(nums))
print(nums)
