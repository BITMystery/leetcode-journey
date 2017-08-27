# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        node = head
        length = 0
        while node:
            length += 1
            node = node.next
        k %= length
        if k == 0:
            return head
        left = right = head
        for _ in xrange(k):
            if not right:
                return head
            right = right.next
        while right.next:
            left, right = left.next, right.next
        new_head = left.next
        left.next = None
        right.next = head
        return new_head