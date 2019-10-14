class Solution:
    '''
    给定不同面额的硬币 coins 和一个总金额 amount。
    编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
    如果没有任何一种硬币组合能组成总金额，返回 -1
    '''

    def coinChange(self, coins, amount: int) -> int:
        '''
        暴力递归
        '''
        if amount == 0:
            return 0
        ans = float('inf')

        for coin in coins:
            if amount - coin < 0:
                continue
            sub = self.coinChange(coins, amount - coin)
            if sub == -1:
                continue
            ans = min(sub + 1, ans)

        return -1 if ans == float('inf') else ans

    def coinChange2(self, coins, amount: int) -> int:
        self.amounts = [-1] * (amount + 1)

        def coinChangeMemo(coins, amount: int) -> int:
            '''
            带备忘录的递归算法
            '''
            if amount == 0:
                return 0
            ans = float('inf')
            if self.amounts[amount] != -1:
                return self.amounts[amount]
            for coin in coins:
                if amount - coin < 0:
                    continue
                sub = coinChangeMemo(coins, amount - coin)
                if sub == -1:
                    continue
                ans = min(sub + 1, ans)

            self.amounts[amount] = -1 if ans == float('inf') else ans
            return self.amounts[amount]

        return coinChangeMemo(coins, amount)

    def coinChange3(self, coins, amount: int) -> int:
        '''
        dp[i]: 兑换i元钱所需要的最小硬币数
        '''
        if amount == 0:
            return 0
        coins = sorted(coins, reverse=True)
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], dp[i - coin] + 1)
        print(dp)
        return -1 if dp[amount] == float('inf') else dp[amount]


if __name__ == "__main__":
    s = Solution()
    print(s.coinChange3([1, 2, 5], 100))
