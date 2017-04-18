import random

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
# Idea: Reservoir Sampling. When visiting the i-th node, set its value as result with probility 1/i. 
# Hence, the probility for remaining any value is 1/1 * 1/2 * 2/3 * 3/4 * ... * (k-1)/k = 1/k, where k is the length of the list.
# Linear time, O(1) space.
class Solution(object):
    h = None
    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.h = head
        

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        res = 0
        count = 1
        node = self.h
        while node:
            r = random.randint(1, count)
            if r == 1:
                res = node.val
            node = node.next
            count += 1
        return res
        


# Your Solution object will be instantiated and called as such:
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
obj = Solution(head)
print obj.getRandom()