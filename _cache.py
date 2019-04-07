class Solution:
    def prefixesDivBy5(self, A):
        rtn = []
        flag = True
        for k in range(len(A)):
            if A[k] == 1:
                tmp = A[:k+1]
                tmp.reverse()
                s = 0
                for i, v in enumerate(tmp):
                    if v == 1:
                        s += 2**i
                if s % 5 == 0:
                    flag = True
                else:
                    flag = False
            rtn.append(flag)
            #print(tmp, s, rtn)
        return rtn

    def baseNeg2(self, N):
        if N is None or N == 0:
            return 0
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
            s+=str(v)
        return s


s = Solution()
print(s.prefixesDivBy5([1, 1, 0, 0, 0, 1, 0, 0, 1]))
print(s.baseNeg2(4))
