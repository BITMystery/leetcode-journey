# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 and l2:
        	if l1.val <= l2.val:
        		head = l1
        	else:
        		head = l2
        else:
        	if not l2:
        		head = l1
        	else:
        		head = l2
        while l1 and l2:
        	if l1.val <= l2.val:
        		while l1.next and l1.next.val <= l2.val:
        			l1 = l1.next
        		tmp = l1
        		l1 = l1.next
        		tmp.next = l2
        	else:
        		while l2.next and l2.next.val < l1.val:
        			l2 = l2.next
        		tmp = l2
        		l2 = l2.next
        		tmp.next = l1
        return head

s = Solution()
l1 = ListNode(1)
l1.next = ListNode(5)
l1.next.next = ListNode(6)
l1.next.next.next = ListNode(7)
l1.next.next.next.next = ListNode(9)
l2 = ListNode(2)
l2.next = ListNode(3)
l2.next.next = ListNode(8)
l2.next.next.next = ListNode(10)
head = s.mergeTwoLists(l1, l2)
while head:
	print head.val
	head = head.next

        