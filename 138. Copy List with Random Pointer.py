# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        index = {}
        node = head
        l = []
        i = 0
        while node:
            index[node] = i
            l.append(RandomListNode(node.label))
            node = node.next
            i += 1
        node = head
        for j in xrange(i):
            l[j].next = l[j + 1] if j < i - 1 else None
            if node.random:
                l[j].random = l[index[node.random]]
            else:
                l[j].random = None
            node = node.next
        return l[0]