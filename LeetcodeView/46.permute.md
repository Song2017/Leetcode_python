class Solution:
    '''
    给定一个没有重复数字的序列，返回其所有可能的全排列
    '''
    def permute(self, nums):
        def dfs(first=0):
            if first == n:
                ans.append(nums.copy())
            for i in range(first, n):
                # split element with index i
                nums[first], nums[i] = nums[i], nums[first]
                # retrive all permute nums-nums[first]
                dfs(first + 1)
                # back track: restore nums
                nums[i], nums[first] = nums[first], nums[i]

        n = len(nums)
        ans = []
        dfs()
        return ans

    def permuteF(self, nums):
        def dfs(nums, cur):
            if len(nums) == 0:
                ans.append(cur)
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i + 1:], cur+[nums[i]])

        ans = []
        dfs(nums, [])
        return ans


s = Solution()
print(s.permuteF([1, 2, 3]))
