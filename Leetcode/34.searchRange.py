class Solution:
    def searchRange(self, nums, target):
        '''
        分别求左右边界
        '''
        if target not in nums:
            return [-1, -1]

        rb, lw, h = 0, 0, len(nums) - 1
        while lw <= h:
            mid = (lw + h) // 2
            if nums[mid] <= target:
                lw += 1
            else:
                h -= 1
        rb = lw
        lw, h = 0, len(nums) - 1
        while lw <= h:
            mid = (lw + h) // 2
            if nums[mid] >= target:
                h -= 1
            else:
                lw += 1
        return [h + 1, rb - 1]

    def binary_search(self, nums, target, right=False):
        lo, hi = 0, len(nums)
        while lo < hi:
            #print("Trying to find %d at [%d, %d]" % (target, lo, hi))
            mid = (lo + hi) // 2
            #print("Comparing target %d with mid %d[#%d]" % (target, nums[mid], mid))
            if target > nums[mid] or (right and target == nums[mid]):
                lo = mid + 1
            else:
                hi = mid
        return lo

    def searchRangeFast(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = self.binary_search(nums, target)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        right = self.binary_search(nums, target, True) - 1
        return [left, right]


s = Solution()
print(s.searchRange([1, 2, 2, 2, 3], 2))
print(s.searchRange([1, 2, 3], 2))
print(s.searchRange([2, 2, 3], 2))
print(s.searchRange([2, 2, 3], 22))
