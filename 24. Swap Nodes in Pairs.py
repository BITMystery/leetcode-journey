# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        cur = head
        res = head.next
        while cur and cur.next:
            tmp = cur.next.next
            cur.next.next = cur
            if tmp:
                cur.next = tmp if not tmp.next else tmp.next
            else:
                cur.next = None
            cur = tmp
        return res if res else head