# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList0(self, head: ListNode) -> ListNode:
        # 当没有或只有一个节点时, 直接返回
        if not head or not head.next:
            return head
        # 不存在第三个节点, 也就是只有两个节点
        elif not head.next.next:
            if head.val > head.next.val:
                head.next.next = head
                head = head.next
                # 此时, 原来的第二个节点为head, 原来的第一个节点为head.next
                # head.next.next指向原来的第二个节点
                head.next.next = None
            return head
        # 快慢指针寻找中点
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # 截断使head所在的子链表只到中点为止, 然后分别递归前后两个子链表
        rhead = slow.next
        slow.next = None
        lf = self.sortList(head)
        lr = self.sortList(rhead)
        # 合并lf, lr, 此时二者均为有序的
        head = cur = ListNode(-1)
        # 子链表有一条不存在则返回另外一条
        while lf and lr:
            if lf.val < lr.val:
                cur.next = lf
                lf = lf.next
            else:
                cur.next = lr
                lr = lr.next
            # 结果链表进行到一个节点
            cur = cur.next
        cur.next = lf or lr
        return head.next

    def sortListArray(self, head: ListNode) -> ListNode:
        nums, cur = [], head
        while cur:
            nums.append(cur.val)
            cur = cur.next
        nums.sort()
        cur = head
        for i in nums:
            cur.val = i
            cur = cur.next
        return head

    def sortListArray2(self, head: ListNode) -> ListNode:
        nums, cur = [], head
        while cur:
            nums.append(cur)
            cur = cur.next
        nums.sort(key=lambda x: x.val)
        head = cur = ListNode(-1)
        for i in nums:
            cur.next = i
            cur = cur.next
        cur.next = None
        return head.next

    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        # fast = head.next: fix 2 nodes maximum recursion
        fast, slow = head.next, head
        # find middle
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next 
        sec = slow.next
        slow.next = None
        # recursion
        front = self.sortList(head)
        second = self.sortList(sec)

        ans = cur = ListNode(-1)
        # merge
        while front and second:
            if front.val > second.val:
                cur.next = front
                front = front.next
            else:
                cur.next = second
                second = second.next
            cur = cur.next
        cur = front or second

        return ans.next


l4 = ListNode(4)
l2 = ListNode(2)
l1 = ListNode(1)
l3 = ListNode(3)
l4.next = l2
l2.next = l1
l1.next = l3


if __name__ == "__main__":
    s = Solution()
    s.sortList(l4)
