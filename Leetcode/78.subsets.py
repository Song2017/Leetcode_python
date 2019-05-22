class Solution:
    # O(n*n!): 单个深度遍历是n!, 做了n次
    def subsets(self, nums):
        def dfs(rest):
            if rest in ans:
                return
            ans.append(rest)
            for i in range(len(rest)):
                dfs(rest[:i] + rest[i + 1:])

        ans = list()
        dfs(nums)
        return ans

    # O((n-1)!)
    def subsetsF(self, nums):
        if not nums:
            return [[]]
        else:
            a = [nums[0]]
            uu = self.subsetsF(nums[1:])
            # + uu: add itself to answer
            ans = [(a + s) for s in uu] + uu
            return ans


s = Solution()
print(s.subsetsF([1, 2, 3]))
