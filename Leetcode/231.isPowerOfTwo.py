class Solution:
    '''
    给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
    '''
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0 or n is None:
            return False

        while n > 1:
            if n > (n >> 1) * 2:
                return False
            n = n >> 1
        return True

    def isPowerOfTwoF(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0
