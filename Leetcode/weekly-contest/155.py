class Solution:
    def minimumAbsDifference(self, arr):
        arr.sort()
        # print(arr)
        lowest = arr[1] - arr[0]
        ans = [[arr[0], arr[1]]]
        for i in range(2, len(arr)):
            prelow = lowest
            tmp = arr[i] - arr[i - 1]
            # print(tmp, lowest, arr[i])
            if tmp < prelow:
                ans = [[arr[i - 1], arr[i]]]
                lowest = tmp
            elif tmp == prelow:
                ans.append([arr[i - 1], arr[i]])
        return ans


s = Solution()
# print(s.minimumAbsDifference([4, 2, 1, 3]))
print(
    s.minimumAbsDifference(
        [-17, 46, 63, 81, -101, -91, 121, -2, 112, -15, -65, -96, 6, -139]))
