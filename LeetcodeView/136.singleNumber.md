class Solution:
    '''
    给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
    说明：你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
    '''

    def singleNumber(self, nums) -> int:
        '''
        排序后, 奇数位上的数应该与其后第一个偶数位数值一样
        '''
        nums.sort()
        cur = 0
        for i, v in enumerate(nums):
            if i % 2 == 0:
                cur = v
            elif cur != v:
                return cur
        return nums[-1]

    def singleNumberF(self, nums) -> int:
        '''
        异或运算的应用
        '''
        from functools import reduce
        return reduce(int.__xor__, nums)


s = Solution()
print(s.singleNumberF([3, 1, 1, 3, -1, -1, 3, 4, 4]))
