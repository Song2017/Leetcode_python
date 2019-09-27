class Solution:
    '''
    有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
    现在要求你戳破所有的气球。每当你戳破一个气球 i 时，你可以获得 nums[left] * nums[i] * nums[right] 个硬币。 
    这里的 left 和 right 代表和 i 相邻的两个气球的序号。
    注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。
    求所能获得硬币的最大数量。
    说明:
    你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。
    0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
    示例:
    输入: [3,1,5,8]
    输出: 167
    解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
         coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
    '''

    def maxCoins_slow(self, nums) -> int:
        '''
        回溯解法, 不适合递归超过12次

        '''
        if nums is None:
            return 0
        self.ret = 0

        def maxCoins_bt(nums, coins):
            n = len(nums)
            if n == 1:
                self.ret = max(nums[-1] + coins, self.ret)
                return

            nums.insert(0, 1)
            nums.append(1)
            for i in range(1, n):
                cur = nums[i]
                tmp = nums[i - 1] * cur * nums[i + 1]
                nums.pop(i)
                maxCoins_bt(nums[1:-1], coins + tmp)
                nums.insert(i, cur)

        maxCoins_bt(nums, 0)
        return self.ret

    def maxCoins(self, nums) -> int:
        '''
        思路: 每次选定一个气球最后点爆,
        选到只剩1个气球的值是一定的,
        回到剩2个气球的状态, 可以通过只剩1个气球的状态推出来
        状态转移方程:
        选定一个气球, 最后点爆.
        dp[i][j]: 点爆从i到j的气球, 可以得到的最大值
        1. 区间慢慢增大的过程中, 我们有很多的区间[i, j], 为了求这些区间内的最大值
        设k在区间 [i, j] 中，假如第k个气球最后被打爆，那么此时区间 [i, j] 被分成了三部分，
        [i, k-1]，[k]，和 [k+1, j]，只要我们之前更新过了 [i, k-1] 和 [k+1, j] 这两个子区间的 dp 值，
        可以直接用 dp[i][k-1] 和 dp[k+1][j]
        2. 接下来求第K个气球获得的值, 因为气球K最后被点爆, 此时[i, k-1] 和 [k+1, j]区间内已经没有气球了
        所以k的值是nums[i - 1] * nums[k] * nums[j + 1]

        '''
        if nums is None:
            return 0
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        n = n - 2
        # 区间内的气球数慢慢增加, 只剩1个气球增加到n个
        for step in range(1, n + 1):
            # 遍历所有的区间
            for i in range(1, n - step + 2):
                j = i + step - 1
                # 求当前区间内的点爆i到j所能获得的最大值
                for k in range(i, j + 1):
                    dp[i][j] = max(
                        dp[i][j], nums[i - 1] * nums[k] * nums[j + 1] +
                        dp[i][k - 1] + dp[k + 1][j])
        # print(dp)
        return dp[1][n]


if __name__ == '__main__':
    s = Solution()
    print(s.maxCoins([3, 1, 5, 8]))
