class Solution:
    '''
    给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
    找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
    例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
    与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2)    
    '''

    def threeSumClosest(self, nums, target: int) -> int:
        '''
        先排序以便应用双指针
        固定一个值, 然后双指针
        '''
        ans, length = float('inf'), len(nums)
        nums.sort()
        for i in range(length):
            # 与前一数组值一致, 则跳过
            # i>0: [0,0,0], 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 数组排过序并且当前索引之前的元素已经取得最小值, 不需要再比较
            left, right = i + 1, length - 1

            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == target:
                    return target
                if abs(s - target) < abs(ans - target):
                    ans = s
                # 移动指针
                if s < target:
                    left += 1
                else:
                    right -= 1
        return ans

    def threeSumClosestF(self, nums, target: int) -> int:
        ans = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            # 排序后, 前面两个值比目标值大则缓存, 返回
            if nums[i] + nums[left] + nums[left + 1] > target:
                ans.append(nums[i] + nums[left] + nums[left + 1])
            # 排序后, 最后面两个值比目标值小则缓存, 返回
            elif nums[i] + nums[right] + nums[right - 1] < target:
                ans.append(nums[i] + nums[right] + nums[right - 1])
            else:
                while left < right:
                    s = nums[i] + nums[left] + nums[right]
                    if s == target:
                        return target
                    ans.append(s)
                    # 移动指针
                    if s < target:
                        left += 1
                    else:
                        right -= 1
        ans.sort(key=lambda x: abs(x - target))
        return ans[0]


so = Solution()
# print(so.threeSum([-1, 23, -5, 6, 77, 1, 0]))
# print(so.threeSumClosest([-1, 2, 1, -4], 1))
print(so.threeSumClosestF([0, 0, 0], 1))
