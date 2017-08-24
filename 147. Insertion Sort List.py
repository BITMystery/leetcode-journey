# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        cur = head.next
        prev = head
        head.next = None
        while cur:
            if prev.val <= cur.val:
                prev.next = cur
                prev = cur
                cur = cur.next
                prev.next = None
                continue
            nxt = cur.next
            cur.next = None
            if cur.val <= head.val:
                cur.next = head
                head = cur
            else:
                tmp = head
                while tmp.next and cur.val > tmp.next.val:
                    tmp = tmp.next
                cur.next = tmp.next
                tmp.next = cur
            cur = nxt
        return head