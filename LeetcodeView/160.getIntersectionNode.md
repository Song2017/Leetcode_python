# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode

        将长的链表的多余的节点先遍历
        """
        if headA is None or headB is None:
            return None
        cura, curb, na, nb = headA, headB, 0, 0
        while cura.next:
            cura = cura.next
            na += 1
        while curb.next:
            curb = curb.next
            nb += 1
        if nb < na:
            cura, curb = headB, headA
        else:
            cura, curb = headA, headB
        ni = abs(na - nb)
        while ni > 0:
            curb = curb.next
            ni -= 1
        ans = None
        while cura and curb:
            if cura == curb:
                ans = cura
                break
            cura = cura.next
            curb = curb.next
        return ans

    def getIntersectionNodeOptm(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode

        将长的链表的多余的节点先遍历
        """
        if headA is None or headB is None:
            return None
        cura, curb, na, nb = headA, headB, 0, 0
        while cura.next:
            cura = cura.next
            na += 1
        while curb.next:
            curb = curb.next
            nb += 1
        if nb < na:
            headA, headB, na, nb = headB, headA, nb, na

        while na < nb:
            headB = headB.next
            nb -= 1

        while headA and headB:
            if headA == headB:
                break
            headA = headA.next
            headB = headB.next
        return headA

    def getIntersectionNodeF(self, headA, headB):
        '''
        如果长度相同，没有交点，在第一轮末尾时，pA和pB会同时为null，这时就相等退出
        如果长度不同，没有交点，会在第二轮末尾同时为null，相等退出
        '''
        if headA is None or headB is None:
            return None
        cura, curb = headA, headB

        while cura != curb:
            cura = headB if cura is None else cura.next
            curb = headA if curb is None else curb.next
        return cura

    def getIntersectionNodeCircle(self, headA, headB):
        if headA is None or headB is None:
            return None
        # 将最后的节点指向B的首节点构造出一个环
        curb = headB
        while curb.next:
            curb = curb.next
        curb.next = headB
        # headB转化为探测环 142
        slow = fast = headA
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                slow = headA
                while slow != fast:
                    slow, fast = slow.next, fast.next
                curb.next = None
                return slow
        curb.next = None
        return None
