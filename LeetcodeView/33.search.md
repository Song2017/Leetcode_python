class Solution:
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
            if (mv >= lv
                    and target < lv) or target > mv >= lv or lv > target > mv:
                left = middle + 1
            else:
                right = middle - 1
        return -1


s = Solution()
print(s.search([4, 5, 6, 7, 0, 1, 2], 5))
