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
        curr = dummy = ListNode(0)
        dummy.next = head
        for _ in xrange(m - 1):
            curr = curr.next
        node1, node2 = curr, curr.next
        curr, prev = node2.next, node2
        for _ in xrange(n - m):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        node1.next = prev
        node2.next = curr
        return dummy.next