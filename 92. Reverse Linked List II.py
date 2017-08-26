# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        left_tail = dummy = ListNode(0)
        dummy.next = head
        for _ in xrange(m - 1):
            left_tail = left_tail.next
        cur = right_head = left_tail.next
        for _ in xrange(n - m):
            nxt = cur.next
            cur.next = nxt.next
            nxt.next = right_head
            right_head = nxt
        left_tail.next = right_head
        return dummy.next
