class Solution:
    def convert(self, s: str, numRows: int) -> str:
        '''
            笨办法: 根据N型字符串每一行的字符在原字符串的索引
            n = 3
            0+ 2*(n-1) 2*0     0   4   8     12
            1+ 2*(n-2) 2*1     1 3 5 7 9  11 13 15
            2+ 2*(n-3) 2*2     2   6   10    14
            n = 4
            0    6      12     6, 6
            1  5 7   11 13     4,2 4,2
            2 4  8 10   14     2,4 2,4
            3    9      15     6, 6
        '''
        if numRows == 1:
            return s

        length, index, ans = len(s), -1, []

        for i in range(numRows - 1, -1, -1):
            index += 1
            str_begin_index, sec = index, False
            while str_begin_index < length:
                if index == 0:
                    sec = False
                if i == 0:
                    sec = True
                ans.append(s[str_begin_index])
                if sec:
                    str_begin_index += 2 * index
                    sec = False
                else:
                    str_begin_index += 2 * i
                    sec = True

        return ''.join(ans)


s = Solution()
print(s.convert("PAYPALISHIRING", 3))
print(s.convert("A", 1))
