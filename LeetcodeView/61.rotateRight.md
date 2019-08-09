# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    '''
    给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
    输入: 1->2->3->4->5->NULL, k = 2
    输出: 4->5->1->2->3->NULL
    '''

    def rotateRight(self, head, k):
        '''
        本质上是将尾部向前数第K个元素作为头，原来的头接到原来的尾上
        '''
        if head is None or head.next is None:
            return head
        cur, n = head, 1
        while cur.next:
            cur = cur.next
            n += 1
        # 尾节点指向首节点
        cur.next, k = head, k % n
        # 定位新的首节点
        first = n - k - 1
        while first > 0:
            head = head.next
            first -= 1
        ans = head.next
        head.next = None
        return ans
