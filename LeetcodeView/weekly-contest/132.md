class Solution:
    d = {1: False}

    def divisorGame(self, N: int) -> bool:

        if N not in self.d:
            found = False
            for i in range(1, N // 2 + 1):
                if N % i == 0:
                    if not self.divisorGame(N - i):
                        self.d[N] = True
                        found = True
                        break
            if not found:
                self.d[N] = False
        # print(self.d)
        return self.d.get(N, False)


s = Solution()
# print(s.divisorGame(6))
print(s.divisorGame(17))
# print(s.removeOuterParentheses("((()())(()()))"))
