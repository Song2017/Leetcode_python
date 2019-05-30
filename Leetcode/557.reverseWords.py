class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        for w in s.split(' '):
            ans.append(w[::-1])
        return ' '.join(ans)

    def reverseWords2(self, s):
        return ' '.join([w[::-1] for w in s.split(' ')])


s = Solution()
print(s.reverseWords("Let's take LeetCode contest"))