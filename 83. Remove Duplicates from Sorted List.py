# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        cur = head
        nxt = head.next
        while nxt:
            if cur.val == nxt.val:
                cur.next = nxt = nxt.next
            else:
                cur = nxt
                nxt = cur.next
        return head