class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = cur = ListNode(0)
        while cur:
            if not l1:
                cur.next = l2
                break
            if not l2:
                cur.next = l1
                break
            if l1.val < l2.val:
                cur.next = l1
                cur, l1 = cur.next, l1.next
            else:
                cur.next = l2
                cur, l2 = cur.next, l2.next
        return dummy.next
