class Solution:
    '''
    一个机器人位于一个 m x n 网格的左上角 (起始点在下图中标记为“Start” )。
    机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角(在下图中标记为“Finish”)。
    问总共有多少条不同的路径
    '''

    def uniquePaths(self, m: int, n: int) -> int:
        '''
        DP: 反向考虑, 到达当前格子的路径数目只能是右面或上面的格子
            所以当前鸽子的数量就是右面或上面的格子路径数目之和
        '''
        dp = [[0] * n] * m
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]

    def uniquePathsF(self, m: int, n: int) -> int:
        '''
        DP: 最上和最右一条的路径数目肯定是1, 所以直接略过
        '''
        dp = [[1] * n] * m
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]

    def uniquePathsFF(self, m: int, n: int) -> int:
        '''
        组合: 机器人一定会走m+n-2步，即从m+n-2中挑出m-1步向下走, 即C((m+n-2)，(m-1))
        '''
        if m < 2 or n < 2:
            return 1
        cache = [1] * (m + n - 2)
        for i in range(1, m + n - 2):
            cache[i] = cache[i-1] * (i + 1) 
        return cache[-1] // (cache[m - 2] * cache[n - 2])


s = Solution()
print(s.uniquePathsFF(7, 3))
