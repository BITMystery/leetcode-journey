# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = l1.val
        num2 = l2.val
        l1 = l1.next
        l2 = l2.next
        while l1:
        	num1 = num1 * 10 + l1.val
        	l1 = l1.next
        while l2:
        	num2 = num2 * 10 + l2.val
        	l2 = l2.next
        s = num1 + num2
        node = ListNode(s%10)
        s /= 10
        while s:
        	next_node = node
        	node = ListNode(s%10)
        	s /= 10
        	node.next = next_node
        return node

s = Solution()
l1 = ListNode(1)
l1.next = ListNode(2)
l2 = ListNode(3)
l = s.addTwoNumbers(l1, l2)
print l.val, l.next.val