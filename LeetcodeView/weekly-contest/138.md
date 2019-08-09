class Solution(object):
    def heightChecker(self, heights) -> int:
        '''
        学校在拍年度纪念照时，一般要求学生按照 非递减 的高度顺序排列。
        请你返回至少有多少个学生没有站在正确位置数量。该人数指的是：
        能让所有学生以 非递减 高度排列的必要移动人数
        '''
        ans, s = 0, sorted(heights)
        for sh, h in zip(heights, s):
            if sh != h:
                ans += 1
        return ans

    def maxSatisfied(self, customers, grumpy, X):
        '''
        今天，书店老板有一家店打算试营业 customers.length 分钟。
        每分钟都有一些顾客（customers[i]）会进入书店，所有这些顾客都会在那一分钟结束后离开。
        在某些时候，书店老板会生气。 如果书店老板在第 i 分钟生气，那么 grumpy[i] = 1，否则 grumpy[i] = 0
        当书店老板生气时，那一分钟的顾客就会不满意，不生气则他们是满意的。
        书店老板知道一个秘密技巧，能抑制自己的情绪，可以让自己连续 X 分钟不生气，但却只能使用一次。
        请你返回这一天营业下来，最多有多少客户能够感到满意的数量
        注意: 生气是1
        先求出已有的满意数量, 然后以X为区间长度, 向左滑动求连续满意的最大数量
        '''
        ans, m, t, n = 0, 0, 0, len(grumpy)
        for i in range(n):
            if grumpy[i] == 0:
                ans += customers[i]
        for i in range(X):
            if grumpy[i] == 1:
                m += customers[i]
        t = m
        for i in range(X, n):
            if grumpy[i] == 1:
                t += customers[i]
            if grumpy[i - X] == 1:
                t -= customers[i - X]
            m = max(m, t)
        return ans + m

    def prevPermOpt1(self, A):
        '''
        给你一个正整数的数组 A（其中的元素不一定完全不同），
        请你返回可在 一次交换（交换两数字 A[i] 和 A[j] 的位置）后得到的、按字典序排列小于 A 的最大可能排列。
        '''
        n = len(A)
        # 一旦存在一次逆序, 就可以找到一个小的排列
        for i in range(n - 2, -1, -1):
            if A[i] > A[i + 1]:
                break
        else:
            return A
        # 要寻找最接近的小排列, 从数位小的方向开始
        # 一旦高数位的值大于低数位的值, 则交换
        for j in range(n - 1, i, -1):
            if A[j] < A[i]:
                break
        A[i], A[j] = A[j], A[i]
        return A

    def rearrangeBarcodes0(self, barcodes):
        barcodes.sort()
        ans, cache = [], []
        ans.append(barcodes.pop())
        while barcodes:
            if barcodes:
                tmp = barcodes.pop()
                if tmp != ans[-1]:
                    ans.append(tmp)
                elif cache and cache[-1] != tmp:
                    ans.append(cache.pop())
                    cache.append(tmp)
                else:
                    cache.append(tmp)
        index = 0
        while cache:
            tmp = cache.pop()
            if ans[0] != tmp:
                ans.insert(0, tmp)
            elif ans[-1] != tmp:
                ans.append(tmp)
            elif ans[index - 1] != tmp and ans[index] != tmp:
                ans.insert(index, tmp)
                index += 1
            else:
                cache.append(tmp)
            index += 1
            index = index % len(ans)
            print(cache, tmp)
        return ans

    def rearrangeBarcodes(self, barcodes):
        '''
        将数组按数值:次数建立hash表, 然后将按出现次数进行排序, 间隔插入
        为防止出现相邻值, 将出现次数最多的数值先开始插入
        '''
        d, ans, index = {}, [0] * len(barcodes), 0
        for i in barcodes:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        s = sorted(d.keys(), key=lambda x: d[x], reverse=True)
        for v in s:
            for _ in range(d[v]):
                ans[index] = v
                index += 2
                if index >= len(barcodes):
                    index = 1

        return ans


s = Solution()
# print(s.maxSatisfied([10, 1, 7], [0, 0, 0], 2))
# print(s.maxSatisfied([9, 10, 4, 5], [1, 0, 1, 1], 1))
# print(s.prevPermOpt1([1, 9, 4, 6, 7]))
print(s.rearrangeBarcodes([1, 1, 1, 1, 2, 2, 3, 3]))
print(s.rearrangeBarcodes([9, 9, 10, 9, 10, 10, 9, 10, 5, 10]))
