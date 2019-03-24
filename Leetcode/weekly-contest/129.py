class Solution:
    def canThreePartsEqualSum(self, A):
        avg = sum(A)/3
        if avg != int(avg):
            return False
        tmp, cnt, idx = 0, 0, 0
        for i, v in enumerate(A):
            tmp += v
            if cnt == 2:
                idx = i
                break
            if tmp == avg:
                tmp = 0
                cnt += 1
        if sum(A[idx:]) == avg:
            return True
        else:
            return False

    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 2 == 0 or K % 5 == 0:
            return -1
        value = 0
        for i in range(1, 10**5+1):
            value = (value*10 + 1) % K
            if value == 0:
                return i
        return -1

    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        Score = 0
        for i, v in enumerate(A):


s = Solution()
print(s.canThreePartsEqualSum([0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]))
print(s.canThreePartsEqualSum([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]))
print(s.smallestRepunitDivByK(49997))