'''
# 快速排序
1. 取基准值,元素按大小左右分区,然后进行递归直到每个分区只有一个元素或为空
2. 排序思想: 分而治之 D&C divide and conquer
3. 递归: 基线条件 不再进行递归的条件 涉及数组时,多是数组为空或只有一个元素
       递归条件 继续调用函数自身的条件
4. O(nlogn) n:每层元素的个数; logn:调用栈的高度.
           O(n):处理每层n个元素的时间; O(logn): 需要处理的层数
5. 单向实现: 简单易懂
    基准值选取: 首位,末位和中位的平均值
6. 双向排序: 提高非随机输入的性能
    不需要额外的空间,在待排序数组本身内部进行排序
    基准值通过random随机选取
'''
import random


# 快速排序
# 取基准值,元素按大小左右分区,然后进行递归直到每个分区只有一个元素或为空
# 排序思想: 分而治之 D&C divide and conquer
# 递归: 基线条件 不再进行递归的条件 涉及数组时,多是数组为空或只有一个元素
#       递归条件 继续调用函数自身的条件
# O(nlogn) n:每层元素的个数; logn:调用栈的高度.
#          O(n):处理每层n个元素的时间; O(logn): 需要处理的层数
def QuickSortNotRepeate(arr):
    arrLen = len(arr)
    if arrLen < 2:
        return arr
    # 基准值为数组首位,末位,中间位数字的平均值
    pivot = (arr[0] + arr[-1] + arr[arrLen // 2]) / 3
    # 推导式简单实现[i, pivot]
    less = [i for i in arr[:] if i <= pivot]
    # 推导式简单实现(pivot, len(arr)]
    greater = [i for i in arr[:] if i > pivot]
    return QuickSortNotRepeate(less) + QuickSortNotRepeate(greater)


# print('QuickSort([90,0,-1,22,3])', QuickSortNotRepeate([0, 1, 2, 3]))


# 用快速排序查找第K大元素(非索引值) 1=<K<=len(arr)
def QuickSortPosK(arr, K):
    # 基准值为数组首位,末位数字的平均值
    if len(arr) == 1:
        return arr[0]
    pivot = (arr[0] + arr[-1]) / 2
    # 推导式简单实现[i, pivot]
    less = [i for i in arr[:] if i <= pivot]
    greater = [i for i in arr[:] if i > pivot]
    lenLess = len(less)
    if lenLess == K:
        return less[-1]
    elif lenLess > K:
        return QuickSortPosK(less[:-1], K)
    elif lenLess < K:
        return QuickSortPosK(greater, K - lenLess)


# print('QuickSortPosK', QuickSortPosK([90, 0, -1, 22, 3, 3, 3], 4))


def QuickSort(arr):
    # 双向排序: 提高非随机输入的性能
    # 不需要额外的空间,在待排序数组本身内部进行排序
    # 基准值通过random随机选取
    # 入参: 待排序数组, 数组开始索引 0, 数组结束索引 len(array)-1
    if arr is None or len(arr) < 1:
        return arr

    def swap(arr, low, upper):
        arr[low], arr[upper] = arr[upper], arr[low]
        return arr

    def QuickSort_TwoWay(arr, low, upper):
        # 小数组排序i可以用插入或选择排序
        # if upper-low < 50 : return arr
        # 基线条件: low index = upper index; 也就是只有一个值的区间
        if low >= upper:
            return arr
        # 随机选取基准值, 并将基准值替换到数组第一个元素
        # swap(arr, low, int(random.uniform(low, upper)))
        temp = arr[low]
        # 缓存边界值, 从上下边界同时排序
        i, j = low, upper
        while True:
            # 第一个元素是基准值, 所以要跳过
            i += 1
            # 在小区间中, 进行排序
            # 从下边界开始寻找大于基准值的索引
            while i <= upper and arr[i] <= temp:
                i += 1
            # 从上边界开始寻找小于基准值的索引
            # 因为j肯定大于i, 所以索引值肯定在小区间中
            while arr[j] > temp:
                j -= 1
            # 如果小索引大于等于大索引, 说明排序完成, 退出排序
            if i >= j:
                break
            swap(arr, i, j)
            
        # 将基准值的索引从下边界调换到索引分割点
        swap(arr, low, j)
        QuickSort_TwoWay(arr, low, j - 1)
        QuickSort_TwoWay(arr, j + 1, upper)
        return arr

    return QuickSort_TwoWay(arr, 0, len(arr) - 1)


if __name__ == "__main__":
    a1 = [3, 5, 6, 7, 8]
    a2 = [2, 2, 2, 2]
    a3 = [4, 3, 2, 1]
    a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    arr_sample = [3, 4, 2, 66, 1, 8, 9, 2, 4, 3]
    QuickSort(a1)
    print(a1)
    QuickSort(a2)
    print(a2)
    QuickSort(arr_sample)
    print(arr_sample)
    QuickSort(a4)
    print(a4)
