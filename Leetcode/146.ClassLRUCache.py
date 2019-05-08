# Definition for singly-linked list.
class DbListNode(object):
    def __init__(self, x, y):
        self.key = x
        self.val = y
        self.next = None
        self.prev = None


class LRUCache:
    '''
    运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。
    它应该支持以下操作： 获取数据 get 和 写入数据 put 。
    获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
    写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。
        当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间
    哈希表+双向链表
    哈希表: 查询 O(1)
    双向链表: 有序, 增删操作 O(1)
    '''

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hkeys = {}
        self.top = DbListNode(None, -1)
        self.tail = DbListNode(None, -1)
        self.top.next = self.tail
        self.tail.prev = self.top

    def get(self, key: int) -> int:

        if key in self.hkeys.keys():
            # 更新结点顺序
            tmp = self.hkeys[key]
            # 跳出原位置
            tmp.next.prev = tmp.prev
            tmp.prev.next = tmp.next
            # 最近用过的置于链表首部
            tn = self.top.next
            self.top.next = tmp
            tmp.prev = self.top
            tmp.next = tn
            tn.prev = tmp

            return self.hkeys[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hkeys.keys():
            tmp = self.hkeys[key]
            tmp.val = value
            # 跳出原位置
            tmp.prev.next = tmp.next
            tmp.next.prev = tmp.prev

            # 最近用过的置于链表首部
            tn = self.top.next
            self.top.next = tmp
            tmp.prev = self.top
            tmp.next = tn
            tn.prev = tmp
        else:
            # 增加新结点至首部
            tmp = DbListNode(key, value)
            self.hkeys[key] = tmp
            # 最近用过的置于链表首部
            tn = self.top.next
            self.top.next = tmp
            tmp.prev = self.top
            tmp.next = tn
            tn.prev = tmp
            if len(self.hkeys.keys()) > self.cap:
                self.hkeys.pop(self.tail.prev.key)
                # 去掉原尾结点
                self.tail.prev.prev.next = self.tail
                self.tail.prev = self.tail.prev.prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

from collections import OrderedDict


class LRUCacheFast:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dic = OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dic:
            val = self.dic[key]
            del self.dic[key]
            self.dic[key] = val
            return val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dic:
            del self.dic[key]
        elif len(self.dic) == self.capacity:
            self.dic.popitem(False)
        self.dic[key] = value
