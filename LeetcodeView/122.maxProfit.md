class Solution:
    '''
    比较前i-1个数的最小值和i的值
    '''

    def maxProfit(self, prices) -> int:
        if prices == []:
            return 0
        pre, ans = prices[0], 0
        for p in prices:
            if p > pre:
                ans += p - pre
            pre = p
        return ans

    def maxProfitF(self, prices) -> int:
        ans = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                ans += prices[i] - prices[i - 1]

        return ans


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
