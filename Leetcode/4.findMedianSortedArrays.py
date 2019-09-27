class Solution:
    def findMedianSortedArraysB(self, nums1, nums2):
        '''
        1. 两个数组是有序的, 所以分别对两个数组采用二分法
            a. 两个数组被分别进行二分, 所以一共有4个子数组n1l, n1r; n2l, n2r
            b. !! 中间分一下，总体的中位数肯定是在二分后4块数据中的两块
        2. 分割点左右两边的值的边界情况:
            a, n1左值 > n2右值: 总体的中位数是两个数组合并后的中位数,
            此时num1的中位数大于等于合并后的中位数, 所以num1要查小的部分 n1l,
            此时num2的中位数小于等于合并后的中位数, 所以num2要查大的部分 n2r,
            b, n2左值 > n1右值: 类似于a.
            c, 左值 < 右值: 因为数组是有序的, 所以, 左边的个数=右边的个数, 二分点就是中位数的位置
        3. 数组长度是偶数的, 分割点左边的值: nums1[(center1 - 1) >> 1]
                            分割点右边的值: nums1[center1 >> 1]
           是奇数时, 二者是相等的
        '''
        n, m = len(nums1), len(nums2)
        # 为防止索引溢出, 将长度小的数组放到nums1
        if n > m:
            return self.findMedianSortedArraysB(nums2, nums1)
        # num1分割点左边的值, num1分割点右边的值, num2分割点左边的值, num2分割点右边的值
        n1left, n1right, n2left, n2right = 0, 0, 0, 0
        # high设为n * 2, 保证了第一次二分时, 从nums1的末尾开始遍历
        low, high = 0, n * 2
        while low <= high:
            # 待比较的num1的长度, 以此得到num1的二分点
            center1 = low + ((high - low) >> 1)
            # 待比较的num2的长度
            center2 = m + n - center1
            # 6,7 & 3,4,5: nums1已经比较完, 说明都比中位数大, 中位数在nums2,
            # num1分割点左边的值是空了, 不会参与到中位数的计算中
            n1left = -float("inf") if center1 == 0 else nums1[(center1 - 1)
                                                              >> 1]
            # 11,12 & 3,4: nums2已经比较完, 说明都比中位数小, 中位数在nums1,
            # num2分割点右边的值空了, 不会参与到中位数的计算中
            n2right = float("inf") if center2 == 2 * m else nums2[center2 >> 1]
            # num1的中位数大于等于合并后的中位数, 所以num1要查小的部分 n1l
            # 11,12 & 0,1,3:
            if n1left > n2right:
                high = center1 - 1
                continue

            n1right = float("inf") if center1 == 2 * n else nums1[center1 >> 1]
            n2left = -float("inf") if center2 == 0 else nums2[(center2 - 1)
                                                              >> 1]
            if n2left > n1right:
                low = center1 + 1
            else:
                break
        # 处理数组长度为偶数/奇数的边界问题
        return (max(n1left, n2left) + min(n1right, n2right)) / 2.0

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        get median for nums1 and nums2, then use quick sort
        """
        nums = nums1 + nums2
        # 长度减1: 解决索引出错
        # 根据取整判断长度是奇偶数
        mid = (len(nums) - 1) / 2.0
        if mid == int(mid):
            rtn = self.QuickSortPosK(nums, int(mid) + 1)
        else:
            rtn = (self.QuickSortPosK(nums,
                                      int(mid) + 2) + self.QuickSortPosK(
                                          nums,
                                          int(mid) + 1)) / 2
        return rtn

    # 用快速排序查找第K大元素(非索引) 1=<K<=len(arr)
    def QuickSortPosK(self, arr, K):
        # 基准值为数组首位,末位,中间位数字的平均值
        if len(arr) == 1:
            return arr[0]
        pivot = arr[-1]
        # 推导式简单实现[i, pivot]
        less = [i for i in arr[:] if i <= pivot]
        greater = [i for i in arr[:] if i > pivot]
        lenLess = len(less)
        if lenLess == K:
            return less[-1]
        elif lenLess > K:
            return self.QuickSortPosK(less[:-1], K)
        elif lenLess < K:
            return self.QuickSortPosK(greater, K - lenLess)

    def findMedianSortedArraysFast(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        nums.sort()
        # 得到的是索引
        mid = (len(nums) - 1) / 2.0
        # 根据取整后的结果判断数组的个数奇偶性
        if mid == int(mid):
            return nums[int(mid)]
        else:
            return (nums[int(mid)] + nums[int(mid) + 1]) / 2.0

    def findMedianSortedArraysS(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        if m > n:
            return self.findMedianSortedArraysS(nums2, nums1)
        shortleft, shortright, longleft, longright = 0, 0, 0, 0

        low, high = 0, 2 * m
        while low <= high:
            scenter = low + (high - low) >> 1
            lcenter = m + n - scenter
            # 短左 > 长右
            shortleft = -float('inf') if scenter == 0 else nums1[(scenter - 1)
                                                                 >> 1]
            longright = float('inf') if lcenter == 2 * m else nums2[lcenter
                                                                    >> 1]
            if shortleft > longright:
                high = scenter - 1
                continue

            shortright = float('inf') if scenter == 2 * n else nums1[scenter
                                                                     >> 1]
            longleft = -float('inf') if lcenter == 0 else nums2[(lcenter - 1)
                                                                >> 1]
            if longleft > shortright:
                low = scenter + 1
            else:
                break

        return (max(shortleft, longleft) + min(shortright, longright)) / 2.0


Solution1 = Solution()
# print(Solution1.findMedianSortedArraysB([], [9, 11]))
# print(Solution1.findMedianSortedArraysB([1, 2], [9, 11]))
print(Solution1.findMedianSortedArraysS([2, 3], [1]))
