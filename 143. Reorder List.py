# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head_left, head_right = head, slow.next
        slow.next = None
        
        #reverse right part
        cur = head_right
        while cur.next:
            nxt = cur.next
            cur.next = nxt.next
            nxt.next = head_right
            head_right = nxt
        
        cur_left, cur_right = head_left, head_right
        while cur_right:
            nxt_left, nxt_right = cur_left.next, cur_right.next
            cur_left.next = cur_right
            cur_right.next = nxt_left
            cur_left, cur_right = nxt_left, nxt_right