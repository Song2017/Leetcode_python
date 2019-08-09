class Solution:
    def search(self, nums, target):
        low, m, h = 0, 0, len(nums) - 1

        while low <= h:
            m = low + ((h - low) >> 1)
            if nums[m] <= target:
                low += 1
            else:
                h -= 1

        if nums[h] == target:
            return h

        return m

    def searchFast(self, nums, target):
        low, h = 0, len(nums) - 1
        while low <= h:
            m = low + ((h - low) >> 1)
            if nums[m] == target:
                return m
            elif nums[m] < target:
                low += 1
            else:
                h -= 1
        return -1


s = Solution()
print(s.search([2, 5], 2))
