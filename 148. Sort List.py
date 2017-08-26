# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        left, right = head, slow.next
        slow.next = None
        left = self.sortList(left)
        right = self.sortList(right)
        dummy = cur = ListNode(0)
        while True:
            if not left:
                cur.next = right
                break
            if not right:
                cur.next = left
                break
            if left.val < right.val:
                cur.next = left
                cur = left
                left = left.next
            else:
                cur.next = right
                cur = right
                right = right.next
        return dummy.next
                