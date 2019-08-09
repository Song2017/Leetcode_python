## SkipList 跳表
### 是什么
    Skip lists are a data structure that can be used in place of balanced trees. 
    Skip lists use probabilistic balancing rather than strictly enforced balancing and as a result the algorithms for insertion and deletion in skip lists are much simpler and significantly faster than equivalent algorithms for balanced trees.
    --William Pugh
跳表一种链表加多级索引的动态数据结构, 通过**随机算法保证平衡性**, 支持快速的插入、删除、查找操作，时间复杂度都是 O(logn).
### 为什么
1. 链表在内存中是离散的, 这使得链表的插入,删除十分便利O(1), 但是查询却只能一个接一个的遍历, 时间复杂度为O(n).
而插入, 删除操作依赖于查找定位目标节点, 因为查找的性能低, 也降低了二者的性能.
2. 如何提高查找的性能, 达到类似数组中二分查找的效果呢, 可以通过添加索引. 
跳表作为一种添加了索引的链表数据结构，可以支持快速的插入、删除、查找操作.
### 怎么做
1. 对一个单链表来讲, 即使存储的数据是有序的, 查找时间复杂度仍然是O(n), 那么如何提高查找效率呢?
既然链表的内存分布是离散的, 我们不能直接在内存中访问, 那么参考二分查找算法思想, 
我们将这些离散的内存指针有规律的抽取组合起来, 逐步缩小指针的个数. 
当每两个结点提取一个结点到上一级(抽出来的那一级叫索引)时, 
**第 k 级索引的结点个数是第 k-1 级索引的结点个数的 1/2，那第 k级索引结点的个数就是 n/(2^k)**
例如, 链表存储有序的1-16个数字. 索引的个数分别为2, 4, 8.
当我们要查12时, 先查到顶层中的9, 接着通过第2层中的9映射到第3层的11, 最后通过11映射到12
    1, , , , , , , ,9,  ,  ,  ,  ,  ,  ,
    1, , , ,5, , , ,9,  ,  ,  ,13,  ,  ,
    1, ,3, ,5, ,7, ,9,  ,11,  ,13,  ,15,
    1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16
![在这里插入图片描述](https://img-blog.csdnimg.cn/2019060509260819.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3NnczU5NTU5NQ==,size_16,color_FFFFFF,t_70)
2. 时间复杂度的计算: 因为抽取数据时是有规律(二选一)的, 所以每层最多只需要比较2次
    索引的高度是log~2~n-1, 加上原始链表为log~2~n. 查找过程为串行的, 时间复杂度为O(2*log~2~n)
此时的空间复杂度为: n/2+n/2\^2 + n/2\^3+...1 = n - 1, 加上原始链表的内存, 空间复杂度为O(2n)
为了节约空间, 我们可以增加每次比较的节点的长度, 当三选一时:
    时间复杂度为O(3*log~3~n), 空间复杂度为n/3+n/3\^2+n/3\^3+...1 = n/2 - 1, 空间复杂度为O(1.5n)
当然在实际的软件开发中，原始链表中存储的有可能是很大的对象，而索引结点只需要存储关键值和几个指针，并不需要存储对象，
所以当对象比索引结点大很多时，那索引占用的额外空间就可以忽略
3. [Redis Source Code](https://github.com/antirez/redis/blob/unstable/src/t_zset.c)
### 插入,删除操作
对于单链表来说, 要进行插入删除操作, 我们需要先通过查找操作定位到目标节点.查找操作的低性能降低了其他操作的性能.
跳表的查找操作时间复杂度为O(mlog~m~n), 定位到目标节点后, 进行插入,删除操作O(1).
只是**跳表还有索引, 如果我们不更新索引，就有可能出现某 2 个索引结点之间数据非常多的情况**。
极端情况下，跳表还会退化成单链表。作为一种动态数据结构，我们需要某种手段来维护索引与原始链表大小之间的平衡.
**红黑树等平衡二叉树通过左右旋来保证平衡性, 而跳表通过一个随机函数，来决定将这个结点插入到哪几级索引中**，
比如随机函数生成了值 K，那我们就将这个结点添加到第一级到第 K 级这 K 级索引中
### 特点
1. 查找, 插入及删除操作的时间复杂度均为O(logn)
2. 按区间查找数据: 跳表可以做到 O(logn) 的时间复杂度定位区间的起点，然后在原始链表中顺序往后遍历就可以了
3. 使用概率均衡技术而不是使用强制性均衡, 实现简单, 可读性好
4. 可以通过改变索引构建策略，有效平衡执行效率和内存消耗
### 实现
```
import random


class SkipListNode(object):
    def __init__(self, val, high=1):
        # 节点存储的值
        self.data = val
        # 节点对应索引层的深度
        self.deeps = [None] * high


class SkipList(object):
    """
        An implementation of skip list.
        The list stores positive integers without duplicates.
        跳表的一种实现方法。
        跳表中储存的是正整数，并且储存的是不重复的。
        Author: Ben
    """

    def __init__(self):
        # 索引层的最大深度
        self.__MAX_LEVEL = 16
        # 跳表的高度
        self._high = 1
        # 每一索引层的首节点, 默认值为None
        self._head = SkipListNode(None, self.__MAX_LEVEL)

    def find(self, val):
        cur = self._head
        # 从索引的顶层, 逐层定位要查找的值
        # 索引层上下是对应的, 下层的起点是上一个索引层中小于插入值的最大值对应的节点
        for i in range(self._high - 1, -1, -1):
            # 同一索引层内, 查找小于插入值的最大值对应的节点
            while cur.deeps[i] and cur.deeps[i].data < val:
                cur = cur.deeps[i]

        if cur.deeps[0] and cur.deeps[0].data == val:
            return cur.deeps[0]
        return None

    def insert(self, val):
        '''
        新增时, 通过随机函数获取要更新的索引层数,
        要对低于给定高度的索引层添加新结点的指针
        '''
        high = self.randomLevel()
        if self._high < high:
            self._high = high
        # 申请新结点
        newNode = SkipListNode(val, high)
        # cache用来缓存对应索引层中小于插入值的最大节点
        cache = [self._head] * high
        cur = self._head

        # 在低于随机高度的每一个索引层寻找小于插入值的节点
        for i in range(high - 1, -1, -1):
            # 每个索引层内寻找小于带插入值的节点
            # ! 索引层上下是对应的, 下层的起点是上一个索引层中小于插入值的最大值对应的节点
            while cur.deeps[i] and cur.deeps[i].data < val:
                cur = cur.deeps[i]
            cache[i] = cur

        # 在小于高度的每个索引层中插入新结点
        for i in range(high):
            # new.next = prev.next \ prev.next = new.next
            newNode.deeps[i] = cache[i].deeps[i]
            cache[i].deeps[i] = newNode

    def delete(self, val):
        '''
        删除时, 要将每个索引层中对应的节点都删掉
        '''
        # cache用来缓存对应索引层中小于插入值的最大节点
        cache = [None] * self._high
        cur = self._head
        # 缓存每一个索引层定位小于插入值的节点
        for i in range(self._high - 1, -1, -1):
            while cur.deeps[i] and cur.deeps[i].data < val:
                cur = cur.deeps[i]
            cache[i] = cur
        # 如果给定的值存在, 更新索引层中对应的节点
        if cur.deeps[0] and cur.deeps[0].data == val:
            for i in range(self._high):
                if cache[i].deeps[i] and cache[i].deeps[i].data == val:
                    cache[i].deeps[i] = cache[i].deeps[i].deeps[i]

    def randomLevel(self, p=0.25):
        '''
        #define ZSKIPLIST_P 0.25      /* Skiplist P = 1/4 */
        https://github.com/antirez/redis/blob/unstable/src/t_zset.c
        '''
        high = 1
        for _ in range(self.__MAX_LEVEL - 1):
            if random.random() < p:
                high += 1
        return high

    def __repr__(self):
        vals = []
        p = self._head
        while p.deeps[0]:
            vals.append(str(p.deeps[0].data))
            p = p.deeps[0]
        return '->'.join(vals)


if __name__ == '__main__':
    sl = SkipList()
    for i in range(100):
        sl.insert(i)
    print(sl)
    p = sl.find(7)
    print(p.data)
    sl.delete(37)
    print(sl)
    sl.delete(37.5)
    print(sl)

```