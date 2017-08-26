# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        node = head
        for _ in xrange(k):
            if not node:
                return head
            node = node.next
        cur = head
        for _ in xrange(k - 1):
            nxt = cur.next
            cur.next = nxt.next
            nxt.next = head
            head = nxt
        cur.next = self.reverseKGroup(cur.next, k)
        return head
