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
        if not head:
            return None
        node = head
        for _ in xrange(k):
            if not node:
                return head
            node = node.next
        cur, new_head = head, head
        for _ in xrange(k - 1):
            nxt = cur.next
            cur.next = nxt.next
            nxt.next = new_head
            new_head = nxt
        cur.next = self.reverseKGroup(cur.next, k)
        return new_head