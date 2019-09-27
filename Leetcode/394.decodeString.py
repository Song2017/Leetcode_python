class Solution:
    '''
    给定一个经过编码的字符串，返回它解码后的字符串。
     编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
     你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
     此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。
     示例:
     s = "3[a]2[bc]", 返回 "aaabcbc".
    s = "3[a2[c]]", 返回 "accaccacc".
    s = "2[abc]3[cd]ef", 返回 "abcabccdcdcdef".    
    '''

    def decodeString_(self, s: str) -> str:
        char, num, chars, nums = '', 0, [], []
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '[':
                nums.append(num)
                # 压栈[前解码的字符串
                chars.append(char)
                num = 0
                char = ''
            elif c == ']':
                char = chars.pop() + char * nums.pop()
            else:
                char += c
        return char

    def decodeString(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return n
        nums, chars = [], []
        num, char, ans = 0, '', ''
        for c in s:
            # 最外层的[]
            if len(nums) == 0:
                ans += char
                char = ''
            if c.isdigit():
                num = num * 10 + int(c)
            elif c.isalpha():
                char = char + c
            elif c == '[':
                nums.append(num)
                # 压栈 3[a2[c]] 中的a
                chars.append(char)
                num = 0
                char = ''
            elif c == ']':
                # a + 2 * c
                char = chars.pop() + nums.pop() * char

        return ans + char


if __name__ == "__main__":
    s = Solution()
    print(s.decodeString_("3[a2[c]d]zxc4[ef]gh"))