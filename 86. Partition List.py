# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        less = less_tail = ListNode(0)
        greater = greater_tail = ListNode(0)
        cur = head
        while cur:
            if cur.val < x:
                less_tail.next = cur
                less_tail = cur
                cur = cur.next
                less_tail.next = None
            else:
                greater_tail.next = cur
                greater_tail = cur
                cur = cur.next
                greater_tail.next = None
        less_tail.next = greater.next
        return less.next