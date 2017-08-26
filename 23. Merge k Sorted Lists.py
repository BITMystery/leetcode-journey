# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        h = [(node.val, node) for node in lists if node]
        heapq.heapify(h)
        dummy = cur = ListNode(0)
        while h:
            val, node = heapq.heappop(h)
            cur.next = node
            cur = node
            node = node.next
            if node:
                heapq.heappush(h, (node.val, node))
        return dummy.next