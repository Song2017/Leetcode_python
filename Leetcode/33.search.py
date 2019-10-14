class Solution:
    '''
    假设按照升序排序的数组在预先未知的某个点上进行了旋转。
    ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
    搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
    你可以假设数组中不存在重复的元素。
    你的算法时间复杂度必须是 O(log n) 级别。
    示例 1:
    输入: nums = [4,5,6,7,0,1,2], target = 0
    输出: 4
    '''

    def search0(self, nums, target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            middle = left + ((right - left) >> 1)
            lv, mv = nums[left], nums[middle]
            # target最小或最大, target大于middle小于left
            # 120: 选0, 012: 选2, 201: 选1
            if mv >= lv > target or target > mv >= lv or lv > target > mv:
                left = middle + 1
            else:
                right = middle
        return left if left == right and nums[left] == target else -1

    def search(self, nums, target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
        left, right = 0, n - 1
        while left <= right:
            middle = left + ((right - left) >> 1)
            lv, mv = nums[left], nums[middle]
            if mv == target:
                return middle
            if mv >= lv > target or target > mv >= lv or lv > target > mv:
                left = middle + 1
            else:
                right = middle - 1
        return -1


s = Solution()
print(s.search([4, 5, 6, 7, 0, 1, 2], 5))
