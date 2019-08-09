class Solution:
    def lastStoneWeight(self, stones) -> int:
        n = len(stones)
        while n > 1:
            n -= 2
            tmp = stones.pop(stones.index(max(stones))) - \
                stones.pop(stones.index(max(stones)))
            if tmp != 0:
                stones.append(tmp)
                n += 1
        return stones[0] if n == 1 else 0

    def removeDuplicates(self, S: str) -> str:
        s = [c + c for c in set(S)]
        while S:
            cnt = 0
            for c in s:
                if c in S:
                    cnt += 1
            if cnt == 0:
                break
            for c in s:
                S = S.replace(c, '')
        return S

    def longestStrChain(self, words) -> int:
        import collections
        words = sorted(words, key=lambda w: len(w))
        f = collections.defaultdict(int)
        ans = 0
        for w in words:
            n = len(w)
            for i in range(n):
                f[w] = max(f[w], f[w[:i] + w[i + 1:]] + 1)
                ans = max(ans, f[w])
        # print(f)
        return ans


s = Solution()
# print(s.removeDuplicates('abbaca'))
print(s.longestStrChain(["a", "ba", "bca", "bda", "bdca"]))
print(
    s.longestStrChain([
        "a", "ba", "bca", "bda", "bdca", "bdcaa", "bdcaaa", "bdcaaaa",
        "bdcaaaaa", "bdcaaaaaa", "bdcaaaaaab", "bdcaaaaaabb", "bdcaaaaaabbb",
        "bdcaaaaaabbbb", "bdcaaaaaabbbbb", "bdcaaaaaabbbbbc",
        "bdcaaaaaabbbbbcc"
    ]))
