from typing import List


class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        ans = [0] * 2
        for coin in coins:
            if coin % 2 == 0:
                ans[0] += 1
            else:
                ans[1] += 1
        if ans[0] == 0 or ans[1] == 0:
            return 0
        return ans[0] if ans[0] < ans[1] else ans[1]

    def longestSubsequence(self, arr, difference: int) -> int:
        ans = {}
        ret = 1
        for v in arr:
            ans[v] = ans.get(v - difference, 0) + 1
            ret = max(ret, ans[v])
        return ret

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        self.ans = 0

        def dfs(i, j, cnt):
            cnt += grid[i][j]
            # print(cnt, i,j)
            self.ans = max(cnt, self.ans)
            grid[i][j] = 0
            for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                tmp_i = i + x
                tmp_j = j + y
                if 0 <= tmp_i < rows and 0 <= tmp_j < cols and grid[tmp_i][tmp_j] > 0:
                    tmp = grid[tmp_i][tmp_j]
                    dfs(tmp_i, tmp_j, cnt)
                    grid[tmp_i][tmp_j] = tmp
            

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    continue
                tmp = grid[i][j]
                dfs(i, j, 0)
                grid[i][j] = tmp
        return self.ans


if __name__ == "__main__":
    s = Solution()
    # print(s.longestSubsequence([4, 12, 10, 0, -2, 7, -8, 9, -9, -12, -12, 8, 8], 0))
    print(s.longestSubsequence([1, 2, 3, 4], 1))
    # print(s.getMaximumGold([[0,6,0],[5,8,7],[0,9,0]]))
