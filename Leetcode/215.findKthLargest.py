class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        '''
        在未排序的数组中找到第 k 个最大的元素。
        输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
        输出: 4
        '''
        # 维护k长度最小堆
        hp = [-2**30] * k
        for n in nums:
            # n值小于最小堆堆顶, 跳过
            if n < hp[0]:
                continue
            # 最小堆堆化O(n)
            # 替换最小堆堆顶,将堆中的最小值提升到堆顶  其他值已经有序
            pos, smallpos = 0, 1
            while smallpos < k:
                rightpos = smallpos + 1
                if rightpos < k and not hp[smallpos] < hp[rightpos]:
                    smallpos = rightpos
                hp[pos] = hp[smallpos]
                pos = smallpos
                smallpos = 2 * pos + 1

            # 前一步是父子节点之间提升最小值,
            # pos重新赋值后, 以pos为叶子节点到根节点之间的元素进行排序.
            while pos > 0:
                parentpos = (pos - 1) >> 1
                parentval = hp[parentpos]
                # 父节点的值大于子节点时, 父节点的值降低到子节点
                if parentval > n:
                    hp[pos] = parentval
                    pos = parentpos
                    continue
                break
            hp[pos] = n

        return hp[0]


s = Solution()
print(s.findKthLargest([3, 2, 1, 5, 6, 4], 2))
