class Solution:
    '''
    给定一个字符串 s ，找出 至多 包含 k 个不同字符的最长子串 T。
    示例 1:
    输入: s = "eceba", k = 2
    输出: 3
    解释: 则 T 为 "ece"，所以长度为 3。
    示例 2:
    输入: s = "aa", k = 1
    输出: 2
    解释: 则 T 为 "aa"，所以长度为 2。
    '''
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        '''
        i: 添加元素到哈希表
        j: 数量达到上限后, 减少哈希表中的元素
        '''
        if not s or not k:
            return 0
        n = len(s)
        memo, j, ans = {}, 0, 0
        for i in range(n):
            memo[s[i]] = memo.get(s[i], 0) + 1
            while len(memo.keys()) > k:
                if memo.get(s[j]) - 1 == 0:
                    memo.pop(s[j])
                else:
                    memo[s[j]] = memo.get(s[j]) - 1
                j=j+1
            ans = max(ans, i-j+1)
            # print(memo, ans, i, j)
        return ans