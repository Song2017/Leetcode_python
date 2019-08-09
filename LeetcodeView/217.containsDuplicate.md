class Solution(object):
    '''
    给定一个整数数组，判断是否存在重复元素。
    如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。    
    '''

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))

    def containsDuplicate2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
            if d[i] > 1:
                return True
        return False

    def containsDuplicateF(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = {}
        for i in nums:
            if i in d:
                return True
            else:
                d[i] = 1
        return False


s = Solution()
print(s.containsDuplicate2([1, 2, 3, 1]))
