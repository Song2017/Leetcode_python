class Solution:
    '''
    给定一个字符串，逐个翻转字符串中的每个单词。
    输入: "  the sky  is blue  "
    输出: "blue is sky the"
    '''

    def reverseWordsBuiltIn(self, s: str) -> str:
        return ' '.join(s.split()[::-1])

    def reverseWords(self, s: str) -> str:
        ib, ie, ary = 0, 0, []
        s += ' '
        # remove multiple spaces
        for i in range(len(s)):
            if s[i - 1] != ' ' and s[i] == ' ':
                ie = i
                ary.append(s[ib:ie])
            elif s[i - 1] == ' ' and s[i] != ' ':
                ib = i
        rtn = ''
        for w in ary[::-1]:
            rtn += (w + ' ')
        return rtn[:-1]


s = Solution()
print(s.reverseWords('the sky  is blue'))
