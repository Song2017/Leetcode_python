class Solution:
    def findDuplicate0(self, nums):
        '''
        给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），
        可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。
        不能更改原数组（假设数组是只读的）。
        只能使用额外的 O(1) 的空间。
        时间复杂度小于 O(n2) 。
        数组中只有一个重复的数字，但它可能不止重复出现一次。
        鸽巢原理, O(n)& O(n)
        '''
        low, high = 1, len(nums) - 1
        while low < high:
            cnt, mid = 0, low + ((high - low) >> 1)
            for i in nums:
                if i <= mid:
                    cnt += 1
            if cnt <= mid:
                low = mid + 1
            else:
                high = mid

        return low

    def findDuplicate(self, nums):
        nl = [0] * len(nums)
        for i in nums:
            if 1 == nl[i]:
                return i
            else:
                nl[i] = 1


s = Solution()
print(s.findDuplicate([1, 3, 4, 2, 2]))
