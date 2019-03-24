# Definition for singly-linked list.
"""
:type head: ListNode
:rtype: bool
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 
如果 pos 是 -1，则在该链表中没有环。
说明：不允许修改给定的链表
证明: 存在环
    两个指针都从表头开始走，slow每次走一步，fast每次走两步，
    !!! 因为fast先进入环，在slow进入之后，如果把slow看作在前面，fast在后面每次循环都向slow靠近1，
        所以一定会相遇，而不会出现fast直接跳过slow的情况
    如果fast遇到null，则说明没有环，返回false；
    如果slow==fast，说明有环，并且此时fast超了slow一圈环的长度(b+c) 
    
设: 1. 从头节点到入环节点长度为a
    2. 从入环的节点到相遇节点长度为b
    3. 从相遇的节点再到达入环节点的长度为c
解法1: 利用结论a=c, 得到O(n)&O(1)级别的方案. 下面先证明a=c
证明: a = c(解法1的前提)
    第一次相遇时fast超了slow一圈环的长度, 也就是b+c, 且fast的速度是slow的2倍
    又因为slow走过的距离是a+b, 所以2(a+b) = a+b + b+c, 得到a=c
由a=c, 我们可以得到:使指针从环内相遇的的节点和头节点同时出发, 最终会在入口节点会合(建议画图理解)
解法2:第一次相遇后，让slow,fast继续走，记录到下次相遇时slow前进的距离, 这就是环的长度。
    因为当fast第二次到达Z点时，fast走了一圈，slow走了半圈，而当fast第三次到达Z点时，
    fast走了两圈，slow走了一圈，正好相遇.
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                start = head
                while start != slow:
                    start, slow = start.next, slow.next
                return start
        return None

    def detectCycleLength(self, head):
        slow, fast = head, head
        if head is None:
            return 0
        cnt, cyclelen = 1, 0
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if cnt == 1:
                if slow == fast:
                    cnt -= 1
            else:
                cyclelen += 1
                if slow == fast:
                    return cyclelen


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l1.next = l2
l2.next = l3
l3.next = l1

s = Solution()
print(s.detectCycle(l1))
print(s.detectCycleLength(l1))
