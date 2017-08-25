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
        if not head or not head.next:
            return True
        slow = head
        fast = head.next
        mid = slow.next
        prev = None
        while fast and fast.next:
            slow.next = prev
            prev = slow
            slow = mid
            mid = mid.next
            fast = fast.next.next
        slow.next = prev
        if not fast:
            slow = slow.next
        while slow:
            if slow.val != mid.val:
                return False
            slow, mid = slow.next, mid.next
        return True
