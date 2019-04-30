
# 堆 
堆是一种特殊的树,常用的存储形式是数组. 有意义的是堆顶元素

## 概念
1. 堆是一个完全二叉树
    这使得堆可以用数组来存储
    除了最后一层,其他层的节点个数都是满的,最后一层的节点都靠左排列
2. 堆中每个节点的值都大于等于（或者小于等于）其左右子节点的值
    去掉了子节点之间的关系限制后, 降低了实现复杂度, 提高了排序性能
    大于: 大顶堆, 小于: 小顶堆
## 实现一个堆
1. 堆的存储
    存储堆的数组, 重点区分元素的值和元素的索引, 我们计算的是元素的索引, 数组索引有下面的规律:
    根节点从第1个位置开始时, 元素的索引值是一致的:
        节点索引为i时, 左子节点:i∗2,右子节点: i∗2+1,父节点: i/2
        例: 值/索引 0 1 2 3 4 5 6 7 8, 此时1所在的索引值为1
        节点: 左子节点, 右子节点 
            1: 2, 3
            2: 4, 5
            3: 6, 7 ...
    根节点从0开始时:
        节点索引为i时, 左子节点索引:i∗2 + 1,右子节点索引: i∗2+2,父节点索引: i-1/2
        例:值: 1 2 3 4 5 6 7 8 _, 此时1所在的元素索引为0
         索引: 0 1 2 3 4 5 6 7 9, 
        节点: 左子节点, 右子节点 
            0(1): 1(2), 2(3)
            1(2): 3(4), 4(5)
            ...
    两种保存方式都是可以的, 但是值和索引保持一致时, 计算和理解都容易很多
2. 堆的操作
    1. 往堆中插入一个元素
        1. 堆化: 堆中插入新的元素后,进行调整,让其重新满足堆的特性的过程
            分类, 从下向上, 从上向下
        2. 插入元素不会出现破坏完全二叉树要求的情况, 一般采用从下向上堆化
            堆限制了父子节点之间的关系, 堆化过程中只要按层比对就可以了
        Code 详见Note 3
        ```
        def heappush(self, nums, item):
            nums.append(item)
            self._siftdown(nums, 0, len(nums) - 1)

        ```
    2. 删除堆顶元素
        1. 根据第二条概念可以知道堆顶元素存储的就是堆中数据的最大值或者最小值
        2. 删除堆顶元素后, 需要子节点进行补足, 迭代到子节点后, 容易出现空洞, 即不满足完全二叉树的情况:
            解决, 直接取最后的叶节点替换到堆顶, 然后从上向下堆化
        3. Code: 详见Note 3
        ```
        def heappop(self, nums):
            tail = nums.pop()
            if nums:
                peak = nums[0]
                nums[0] = tail
                self._siftup(nums, 0)
                return peak
            return tail
        ```
## 实现堆排序
1. 建堆
    1. 从前向后: 假设堆中只有一个数据, 然后将下标从 2 到 n 的数据依次插入到堆中
    2. 从后向前: 
        堆的存储数组顺序是按层排序,也就是说已完成排序堆的数组后面的数据是叶子节点, 
        再按照完全二叉树的定义, 叶子节点的下标是从n/2+1开始的, 
        我们只需要从n/2开始, 堆化到下标为1的数据就可以了
    3. 建堆的时间复杂度:  
        因为堆树每层内部的节点之间没有顺序关系, 高层的节点排序要经过低层节点, 
        所以时间复杂可以简单的记做:每层的节点数*层的高度之和
        设: 树的高度为h, 节点数为n. 已知: h = log2n
            因为叶子节点不需要进行比较, 所以不需要计算 h=0
            A: S = 2^0 * h + 2^1 * (h-1) + 2^2 * (h-2) + ... 2^(h-1) * 1
            B: 2*S =         2^1 * (h) + 2^2 * (h-1) + ...   2^(h-1) * 2  + 2^(h)
            B - A = S = -h + 2^1 + 2^2 + ... 2^(h-1) + 2^(h) = -h + (2^h -2) + 2^h = 2^(h+1) - h - 2
           将h=log2n, 代入S, 得到 S = 2*n - log2n -2
           也就是S: O(n)
    4. Code 详见Note 3
        ```
        def heapify(nums):
            '''
            小顶堆堆化, 索引从0开始, 从后向前的方式堆化
            '''
            n = len(nums)
            # 根据完全二叉树的特性, 只需要排序前1/2数组
            for i in reversed(range(n // 2)):
                self._siftup(nums, i)
        ```           
2. 排序
    以大顶堆为例, 堆化完成后第一个元素就是最大的值, 第一个元素已经完成了排序. O(n)
    将最后一个元素与第一个元素互换位置, 再进行1到第n-1个元素范围的排序, 
        因为其他元素都是有序的, 只需要对现在的第一个元素进行排序
        根据堆的定义, 最多需要进行 (堆的高度-1次) 比较, 交换排序范围内的首元素与最后一个元素. O(logn)
    迭代交换排序范围内首元素与最后的元素, 当只剩一个元素时, 就完成了堆的排序. O(nlogn)
3. 时间复杂度
    根据堆排序的过程, 首次全部元素的堆化需要O(n), 剩余元素的排序过程需要O(nlogn).
    二者是串联的关系, 取高的时间复杂度, 也就是O(nlogn)
4. 稳定性
    因为存在交换排序范围内首元素和最后一个元素, 所以存在交换相同数值的原始相对顺序
5. 原地排序
    我们只需要将原始的堆数组划分为待排序区域与已排序区域, 再加上个别的临时存储空间, 
    所以是原地排序
## 堆的应用
### 优先级队列
优先级队列中,数据的出队顺序不是先进先出,而是按照优先级来,优先级最高的,最先出队.
实现一个优先级队列方法有很多,但是用堆来实现是最直接的.很多时候,它们只是概念上的区分而已.
往优先级队列中插入一个元素,就相当于往堆中插入一个元素;从优先级队列中取出优先级最高的元素,就相当于取出堆顶元素.
1. 合并有序小文件
假设我们有 100 个小文件,每个文件的大小是 100MB,每个文件中存储的都是有序的字符串.我们希望将这些 100 个小文件合并成一个有序的大文件.
解: 建立长度为100的最小堆, 进行堆化, 时间复杂度为O(n)
取出堆顶后,放入到大文件中, 然后从对应的文件中取最小字符串, 进行堆化O(logn), 
依次循环, 直到堆为空
2. 高性能定时器
按照任务设定的执行时间,将这些任务存储在优先级队列中,队列首部（也就是小顶堆的堆顶）存储的是最先执行的任务.然后拿队首任务的执行时间点,与当前时间点相减,得到一个时间间隔 T.
这个时间间隔 T 就是,从当前时间开始,需要等待多久,才会有第一个任务需要被执行.从当前时间点到（T-1）秒这段时间里,定时器都不需要做任何事情.
当 T 秒时间过去之后,定时器取优先级队列中队首的任务执行.然后再计算新的差值, 作为新的等待时间, 依次循环/
### TOP K
根据数据集合是否发生改变, 将Top K 的问题抽象成两类.
1. 静态数据
我们可以维护一个大小为 K 的小顶堆,顺序遍历数组,从数组中取出取数据与堆顶元素比较.
如果比堆顶元素大,我们就把堆顶元素删除,并且将这个元素插入到堆中;
如果比堆顶元素小,则不做处理,继续遍历数组.这样等数组中的数据都遍历完之后,堆中的数据就是前 K 大数据了.
遍历数组需要 O(n) 的时间复杂度,一次堆化操作需要 O(logK) 的时间复杂度,所以最坏情况下,n 个元素都入堆一次,所以时间复杂度就是 O(nlogK).
    *Leetcode 215, 代码参见Note 4*
2. 动态数据, 实时 Top K
例如, 一个数据集合中有两个操作,一个是添加数据,另一个询问当前的前 K 大数据.
如果每次询问前K大数据,我们都基于当前的数据重新计算的话,那时间复杂度就是O(nlogK),n表示当前的数据的大小.
实际上,我们可以一直都维护一个 K 大小的小顶堆,当有数据被添加到集合中时,我们就拿它与堆顶的元素对比.
如果比堆顶元素大,我们就把堆顶元素删除,并且将这个元素插入到堆中;如果比堆顶元素小,则不做处理.这样,只是最坏情况时间复杂度为O(nlogK)
    *Leetcode 703, 代码参见Note 5: heapq module*
### 求中位数
求动态数据集合中的中位数.
1. 静态数据
中位数是固定的,我们可以先排序,第 n/2 个数据就是中位数,尽管排序的代价比较大,但是边际成本会很小
2. 动态数据
中位数在不停地变动, 每次都要排序的话, 效率就变低了. 借助堆这种数据结构,我们不用排序,就可以非常高效地实现求中位数操作.
解决: 我们需要维护两个堆,一个大顶堆,一个小顶堆.大顶堆中存储前半部分数据,小顶堆中存储后半部分数据,且小顶堆中的数据都大于大顶堆中的数据.
我们约定, 如果有n个数据, 偶数情况下, 二者均保存n/2个数据; 技术情况下, 大顶堆多保存一个.这时, 大顶堆中的堆顶元素就是我们要找的中位数.
当数据动态添加时, 可能会出现不符合约定的情况, 这是需要从一个堆中不停地将堆顶元素移动到另一个堆,通过这样的调整,来让两个堆中的数据满足上面的约定.
插入数据因为需要涉及堆化,所以时间复杂度变成了 O(logn),但是求中位数我们只需要返回大顶堆的堆顶元素就可以了,时间复杂度是 O(1), 总的时间复杂度级别为O(logn)
### 堆排序
堆排序是一种原地的、时间复杂度为 O(nlogn) 的排序算法
思考: 堆排序比快速排序的时间复杂度稳定,但是,为什么在实际的软件开发中,快速排序的性能要比堆排序好

## Note
1. 为什么快速排序要比堆排序性能好
快速排序,平均情况下,它的时间复杂度为 O(nlogn).
这两种排序算法的时间复杂度都是 O(nlogn),甚至堆排序比快速排序的时间复杂度还要稳定,
快速排序的基准值选取不合适时, 极端情况下会退化到O(n^2). 但是,为什么在实际的软件开发中,快速排序的性能要比堆排序好呢
    堆排序数据访问的方式没有快速排序友好
    快速排序的数据是顺序访问的.而对于堆排序来说,数据是跳着访问的.
        快速排序进行局部的顺序访问,对 CPU的缓存机制 是友好的.
2. CPU的缓存机制
    CPU每次从内存读取数据并不是只读取那个特定要访问的地址,而是读取一个数据并保存到CPU缓存中,然后下次访问内存数据的时候就会先从CPU缓存开始查找,如果找到就不需要再从内存中取.
    这样就实现了比内存访问速度更快的机制,也就是CPU缓存的意义:为了弥补内存访问速度过慢与CPU执行速度快之间的差异而引入
3. 最小堆堆化, 插入, 删除
    ```
    def heapify(nums):
        '''
        小顶堆堆化, 索引从0开始, 从后向前的方式堆化
        '''
        n = len(nums)
        # 根据完全二叉树的特性, 只需要排序前1/2数组
        for i in reversed(range(n // 2)):
            self._siftup(nums, i)


    def heappush(nums, item):
        nums.append(item)
        self._siftdown(nums, 0, len(nums) - 1)


    def heappop(nums):
        tail = nums.pop()
        if nums:
            peak = nums[0]
            nums[0] = tail
            self._siftup(nums, 0)
            return peak
        return tail


    def _siftup(nums, pos):
        '''
        将pos节点的子节点中的最小值提升到pos位置
        '''
        endpos, startpos, startval, smallpos = \
        len(nums), pos, nums[pos], 2 * pos + 1
        while smallpos < endpos:
            # smallpos: 子节点中数值小的节点索引
            rightpos = smallpos + 1
            if rightpos < endpos and not nums[smallpos] < nums[rightpos]:
                smallpos = rightpos
            # 将子节点中小的值提升到父节点
            nums[pos] = nums[smallpos]
            pos = smallpos
            smallpos = 2 * pos + 1
        # 此时pos位置的节点的值已经替换到startpos
        # 互换起始排序节点及其最小子节点的值
        nums[pos] = startval
        # pos: 最小子节点的索引
        self._siftdown(nums, startpos, pos)


    def _siftdown(nums, startpos, pos):
        '''
        以pos为叶子节点, start为根节点之间的元素进行排序. 将pos叶子节点交换到正确的排序位置
        操作: 父节点的值大于子节点时, 父节点的值降低到子节点
        '''
        startval = nums[pos]
        while pos > startpos:
            parentpos = (pos - 1) >> 1
            parentval = nums[parentpos]
            # 父节点的值大于子节点时, 父节点的值降低到子节点
            # 排序索引上升为父节点
            if parentval > startval:
                nums[pos] = parentval
                pos = parentpos
                continue
            break
        # pos: 值大于子节点值中的最深父节点索引
        nums[pos] = startval
    ```
4. findKthLargest
```
    class Solution:
        def findKthLargest(self, nums, k: int) -> int:
            '''
            在未排序的数组中找到第 k 个最大的元素.
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
```
5. KthLargest
```
    #! /usr/bin/evn python
    # coding:utf-8
    from heapq import *


    class KthLargest:
        '''
        设计一个找到数据流中第K大元素的类（class）.注意是排序后的第K大元素,不是第K个不同的元素.
        你的 KthLargest 类需要一个同时接收整数 k 和整数数组nums 的构造器,它包含数据流中的初始元素.
        每次调用 KthLargest.add,返回当前数据流中第K大的元素.
        int k = 3;
        int[] arr = [4,5,8,2];
        KthLargest kthLargest = new KthLargest(3, arr);
        kthLargest.add(3);   // returns 4
        你可以假设 nums 的长度≥ k-1 且k ≥ 1.
        '''

        def __init__(self, k: int, nums):
            self.hp = [-2**30] * k
            heapify(self.hp)
            for n in nums:
                heappushpop(self.hp, n)

        def add(self, val: int) -> int:
            heappushpop(self.hp, val)
            rtn = heappop(self.hp)
            heappush(self.hp, rtn)
            return rtn


    # Your KthLargest object will be instantiated and called as such:
    # obj = KthLargest(k, nums)
    # param_1 = obj.add(val)

    # s = KthLargest(3, [4, 5, 8, 2])
    # print(s.add(3))
    # print(s.add(5))
    # print(s.add(10))
    s = KthLargest(1, [])
    print(s.add(-3))
    print(s.add(-2))
    print(s.add(-4))
```