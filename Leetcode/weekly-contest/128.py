class Solution:
    def bitwiseComplement(self, N: int) -> int:
        return ((1 << len(bin(N)[2:])) - 1) ^ N

    def numPairsDivisibleBy60(self, time) -> int:
        if time is None or len(time) <= 1:
            return 0
        count = 0
        pairs = {}
        for t in time:
            if t in pairs.keys():
                pairs[t] += 1
            else:
                pairs[t] = 1
        lstKeys = list(pairs.keys())
        length = len(lstKeys)
        for i in range(length):
            # 二者的和能整除60, 二者又是相等的, 只需要整除30
            if lstKeys[i] % 30 == 0 and pairs[lstKeys[i]] >= 2:
                count += (pairs[lstKeys[i]] * (pairs[lstKeys[i]] - 1)) / 2
                #print(111, lstKeys[i] , count)
            for j in range(i + 1, length):
                if (lstKeys[i] + lstKeys[j]) % 60 == 0:
                    count += pairs[lstKeys[i]] * pairs[lstKeys[j]]
                    #print(222, lstKeys[i] , lstKeys[j], count)
        return count

    def numPairsDivisibleBy60R(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        import collections
        c = collections.Counter()
        for num in time:
            c[num % 60] += 1
        ans = 0
        for num in time:
            num %= 60
            other = c[(60 - (num % 60)) % 60]
            if num == 30 or num == 0:
                other -= 1
            ans += other
        return ans / 2


s = Solution()
#print(s.numPairsDivisibleBy60([30, 20, 150, 100, 40]))
print(
    s.numPairsDivisibleBy60([
        265, 20, 346, 463, 10, 1, 163, 189, 345, 390, 212, 498, 281, 308, 482,
        447, 217, 318, 239, 374, 449, 298, 213, 2, 230, 5, 500, 300, 390, 139
    ]))
print(
    s.numPairsDivisibleBy60R([
        265, 20, 346, 463, 10, 1, 163, 189, 345, 390, 212, 498, 281, 308, 482,
        447, 217, 318, 239, 374, 449, 298, 213, 2, 230, 5, 500, 300, 390, 139
    ]))
