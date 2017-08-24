# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        l = 0
        node = head
        while node:
            node = node.next
            l += 1
        node = head
        for i in xrange((l + 1) / 2):
            node = node.next
        prev = None
        cur = node
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True