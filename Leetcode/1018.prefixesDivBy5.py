class Solution:
    def prefixesDivBy5(self, A):
        '''
        输入：[0,1,1]
        输出：[true,false,false]
        解释：
        输入数字为 0, 01, 011；也就是十进制中的 0, 1, 3 。只有第一个数可以被 5 整除，因此 answer[0] 为真
        '''
        rtn, s = [False] * len(A), 0
        for i, v in enumerate(A):
            # 二进制求和
            s = (s * 2 + v) % 5
            if s % 5 == 0:
                rtn[i] = True

        return rtn
