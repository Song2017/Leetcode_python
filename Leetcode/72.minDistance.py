class Solution:
    '''给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。

    你可以对一个单词进行如下三种操作：

    插入一个字符
    删除一个字符
    替换一个字符
    示例 1:

    输入: word1 = "horse", word2 = "ros"
    输出: 3
    解释: 
    horse -> rorse (将 'h' 替换为 'r')
    rorse -> rose (删除 'r')
    rose -> ros (删除 'e')
    '''

    def minDistance(self, word1: str, word2: str) -> int:
        '''
        dp[i][j] 代表 word1 到 i 位置转换成 word2 到 j 位置需要最少步数
        所以，
        当 word1[i] == word2[j]，dp[i][j] = dp[i-1][j-1]；
        当 word1[i] != word2[j]，
        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        word1为修改的对象,
            dp[i-1][j-1] 表示替换操作，将word1[i]替换为word2[j]
            dp[i-1][j] 表示删除操作，dp[i][j-1] 表示插入操作

        第一行，是 word1 为空变成 word2 最少步数，就是插入操作
        第一列，是 word2 为空，需要的最少步数，就是删除操作
        '''
        n1 = len(word1) + 1
        n2 = len(word2) + 1
        # if n1 == 1 or n2 == 1:
        #     return n1 + n2 - 2
        dp = [[0] * n2 for _ in range(n1)]

        for i in range(n1):
            dp[i][0] = i
        for j in range(n2):
            dp[0][j] = j
        # print(dp)

        for i in range(n1 - 1):
            for j in range(n2 - 1):
                if word1[i] == word2[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    dp[i + 1][j + 1] = min(dp[i][j], dp[i + 1][j],
                                           dp[i][j + 1]) + 1
        # print(dp)
        return dp[-1][-1]


if __name__ == "__main__":
    s = Solution()
    print(s.minDistance("horse", "ros"))