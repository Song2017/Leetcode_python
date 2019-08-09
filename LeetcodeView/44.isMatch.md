class Solution:
    '''
    给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
    '?' 可以匹配任何单个字符。
    '*' 可以匹配任意字符串（包括空字符串）。
    两个字符串完全匹配才算匹配成功。
    说明:
    s 可能为空，且只包含从 a-z 的小写字母。
    p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
    输入: s = "acdcb" p = "a*c?b" 输入: false
    输入: s = "adceb" p = "*a*b" 输出: true
    解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
    '''

    def isMatch(self, s: str, p: str) -> bool:
        '''
        思路: 动态规划, 沿着匹配串和字符串构成矩阵的对角线传递状态
        1. 状态矩阵的首行与首列对应于空字符与空匹配符
        2. 对角线意味着匹配串是否匹配对应的字符串
        '''
        ns = len(s)
        np = len(p)

        dp = [[False] * (np + 1) for _ in range(ns + 1)]
        dp[0][0] = True
        # 匹配空字符串的情况, 匹配串为空时已经为False, 不再更新
        for i in range(1, np + 1):
            # 根据规则, *前必存在一个字符, 则当前为*时, 其状态与前2的状态一致
            if p[i - 1] == '*' and dp[0][i - 1]:
                dp[0][i] = True
        # 更新状态矩阵
        for i in range(1, ns + 1):
            for j in range(1, np + 1):
                # i,j是矩阵的行与列, 对应到匹配串和字符串的索引要-1
                # 匹配串与字符串匹配(相等或为.)传递状态
                if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                # 匹配串中 * 字符特殊处理
                elif p[j - 1] == '*':
                    # 根据规则, *前不需要再跟字符, 所以传递单字符及多字符的状态, 空字符串已经被多字符所覆盖
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
        # for a in dp:
        #     print(a)
        return dp[ns][np]

    def isMatchF(self, s: str, p: str) -> bool:
        i, j = 0, 0
        # imatch表示s串在p中遇到*时不断尝试的索引
        # jstar记录*在p中的索引
        imatch, jstar = -1, -1
        ns, np = len(s), len(p)
        # 遍历完s, p可以还有
        while i < ns:
            # 字符串匹配的情况下, p,s同时前进
            if j < np and (p[j] == s[i] or p[j] == '?'):
                i += 1
                j += 1
            # p中遇到*, 记录下此时两个串中字符的位置
            elif j < np and p[j] == '*':
                jstar = j
                imatch = i
                j += 1
            # 存在*的情况下, 作为p串中*的回溯点
            elif imatch > -1:
                # !! 回溯点
                j = jstar + 1
                imatch += 1
                i = imatch
            else:
                return False
        # s已经遍历完, 如p中剩余的字符存在非*, 则为false
        for c in p[j:]:
            if c != '*':
                return False
        return True


s = Solution()
# print(s.isMatch('acdcb', 'a*c?b'))
# print(s.isMatch('adceb', '*a*b'))
print(s.isMatchF('abcbcd', 'a*cd'))
print(s.isMatchF('aa', '*'))
print(s.isMatchF('aa', 'a'))
