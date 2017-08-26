# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        dummy1, dummy2 = ListNode(0), ListNode(0)
        dummy1.next, dummy2.next = l1, l2
        head = l1
        l1, l2 = dummy1, dummy2
        while True:
            l1.val += l2.val + carry
            if l1.val > 9:
                l1.val -= 10
                carry = 1
            else:
                carry = 0
            if not l1.next and not l2.next:
                if carry:
                    l1.next = ListNode(1)
                break
            elif not l1.next:
                if carry:
                    l1.next = ListNode(1)
                    carry = 0
                else:
                    l1.next = l2.next
                    break
            elif not l2.next:
                if carry:
                    l2.next = ListNode(1)
                    carry = 0
                else:
                    break
            l1, l2 = l1.next, l2.next
        return head