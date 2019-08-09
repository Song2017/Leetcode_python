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

    def baseNeg2(self, N):
        if N is None or N == 0:
            return "0"
        rtn = []
        vr = 0
        while N != 0 and N != 1:
            # print(N, vr)
            vr = N // -2
            if -2 * vr == N:
                rtn.append(0)
            elif -2 * vr < N:
                rtn.append(1)
            else:
                rtn.append(1)
                vr += 1
            N = vr
        rtn.append(N)
        rtn.reverse()
        if rtn[0] == 0:
            rtn = rtn[1:]
        s = ''
        for v in rtn:
            s += str(v)
        return s
