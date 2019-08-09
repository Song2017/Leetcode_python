class Solution:
    def reverse(self, x: int) -> int:
        s, t = list(str(abs(x)).rstrip('0')), 0
        for i, w in enumerate(s):
            t += 10**i * int(w)
        if x < 0:
            t = -t
        if t < -2**31 or t > (2**31 - 1):
            return 0
        return t

    def reverseF(self, x: int) -> int:
        rtn = 0
        while x != 0:
            ln = x % 10 - 10 if x < 0 and x % 10 != 0 else x % 10
            x = int(x / 10)
            if rtn * 10 > (2**31 - 1) or rtn * 10 < -2**31:
                return 0
            rtn = 10 * rtn + ln
        return rtn


s = Solution()
print(s.reverseF(-123000))