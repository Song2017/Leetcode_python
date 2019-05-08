class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1: 
            return x
        pre, rtn = 0, 1.1
        while abs(rtn - pre) > 1:
            pre, rtn = rtn, (rtn + x / rtn) / 2
        return int(rtn)