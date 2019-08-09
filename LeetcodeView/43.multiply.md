class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        num1 = [int(i) for i in num1]
        num2 = [int(i) for i in num2]
        num1.reverse()
        num2.reverse()
        ans = 0
        for j, n2 in enumerate(num2):
            d = 0
            for i, n1 in enumerate(num1):
                c = n1 * n2 * 10 ** i
                d = d + c
            ans += d * 10 ** j
        return str(ans)


s = Solution()
print(s.multiply('123', '456'))
