class Solution:
    def canThreePartsEqualSum(self, A) :
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
s = Solution()
print(s.canThreePartsEqualSum([0,2,1,-6,6,7,9,-1,2,0,1]))
print(s.canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1]))
