# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
    示例：
    给定一个链表: 1->2->3->4->5, 和 n = 2.
    当删除了倒数第二个节点后，链表变为 1->2->3->5.
    说明：
    给定的 n 保证是有效的。
    进阶：
    你能尝试使用一趟扫描实现吗？ 
    """

    def removeNthFromEnd0(self, head: ListNode, n: int) -> ListNode:
        """
        Maintain two pointers and update one with a delay of n steps.
        """
        root = delay = cur = ListNode(-1)
        cur.next = head
        while cur:
            cur = cur.next
            n -= 1
            if n > -2:
                continue
            delay = delay.next
        delay.next = delay.next.next
        return root.next

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        root = ListNode(-1)
        root.next = head
        cur, start = root, root

        while n:
            n -= 1
            cur = cur.next
        while cur.next:
            cur = cur.next
            start = start.next

        start.next = start.next.next
        return root.next
