class Solution:
    def twoCitySchedCost(self, costs):
        '''
        公司计划面试 2N 人。第 i 人飞往 A 市的费用为 costs[i][0]，飞往 B 市的费用为 costs[i][1]。
        返回将每个人都飞到某座城市的最低费用，要求每个城市都有 N 人抵达。

        求最小和, 限制了分组的数量: 以A为标准求和, 加上B与A的差值
        note: 不能分开考虑A及B, 应该从最终的结果出发
        '''
        diff = list(map(lambda x: x[1] - x[0], costs))
        ans = sum(map(lambda x: x[0], costs))
        diff.sort()
        for i in range(len(diff)//2):
            ans += diff[i]
        return ans

    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int):
        '''
        1030. 距离顺序排列矩阵单元格
        给出 R 行 C 列的矩阵，其中的单元格的整数坐标为 (r, c)，满足 0 <= r < R 且 0 <= c < C。
        另外，我们在该矩阵中给出了一个坐标为 (r0, c0) 的单元格。
        返回矩阵中的所有单元格的坐标，并按到 (r0, c0) 的距离从最小到最大的顺序排，
        其中，两单元格(r1, c1) 和 (r2, c2) 之间的距离是曼哈顿距离，|r1 - r2| + |c1 - c2|。
        （你可以按任何满足此条件的顺序返回答案。）
        '''
        ret = [[r, c] for r in range(R) for c in range(C)]
        ret.sort(key=lambda x: abs(x[0]-r0) + abs(x[1] - c0))
        return ret

    def maxSumTwoNoOverlap(self, A, L: int, M: int) -> int:
        '''
        两个非重叠子数组的最大和
        给出非负整数数组 A ，返回两个非重叠（连续）子数组中元素的最大和，子数组的长度分别为 L 和 M。
        （这里需要澄清的是，长为 L 的子数组可以出现在长为 M 的子数组之前或之后。）
        从形式上看，返回最大的 V，而 V = (A[i] + A[i+1] + ... + A[i+L-1]) + (A[j] + A[j+1] + ... + A[j+M-1])
        并满足下列条件之一：
        0 <= i < i + L - 1 < j < j + M - 1 < A.length, 或0 <= j < j + M - 1 < i < i + L - 1 < A.length.
        '''
        sumary = [0]
        n = len(A)
        ret = 0
        for i in range(n):
            sumary.append(sumary[i] + A[i])

        for i in range(n):
            for j in range(n):
                if i + L <= n and j+M <= n and (i+L <= j or j + M <= i):
                    ret = max(ret, sumary[i+L] -
                              sumary[i] + sumary[j+M] - sumary[j])
        return ret

    def __init__(self, words: List[str]):
        
    def query(self, letter: str) -> bool:
        '''
        按下述要求实现 StreamChecker 类：
        StreamChecker(words)：构造函数，用给定的字词初始化数据结构。
        query(letter)：如果存在某些 k >= 1，可以用查询的最后 k个字符（按从旧到新顺序，包括刚刚查询的字母）
        拼写出给定字词表中的某一字词时，返回 true。否则，返回 false
        '''


s = Solution()
# s.twoCitySchedCost([[10, 20], [30, 200], [400, 50], [30, 20]])
# print(s.allCellsDistOrder(1, 2, 0, 0))
