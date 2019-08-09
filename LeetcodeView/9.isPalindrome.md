class Solution:
    def isPalindrome(self, x: int) -> bool:
        '''
        判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
        '''
        if x < 0:
            return False
        o, s = x, 0
        while x > 0:
            r = x % 10
            x = x // 10
            s = s * 10 + r
        return s == o


s = Solution()
print(s.isPalindrome(121))