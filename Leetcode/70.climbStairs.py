class Solution:
    def __init__(self):
        self.cache = {}

    def climbStairs1(self, n: int) -> int:
        if n == 1:
            self.cache[1] = 1
        elif n == 2:
            self.cache[2] = 2
        elif n not in self.cache.keys():
            # 若已被缓存,则返回缓存值; 若无, 则获取前两次的递归值
            # 因为进行了缓存, 前两次的递归值不需要再递归获取
            self.cache[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.cache[n]

    def climbStairsFast(self, n):
        """
        :type n: int
        :type n: int
        :rtype: int
        """

        cache = {}

        def rclimbStairs(n):
            if n < 1:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 2
            if n in cache:
                result = cache[n]
            else:
                result = rclimbStairs(n - 1) + rclimbStairs(n - 2)
                cache[n] = result
            return result

        return rclimbStairs(n)

    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        if n <= 2:
            return n
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]
