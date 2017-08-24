# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, nums):
        if not nums:
            return None
        mid = len(nums) / 2
        root = TreeNode(nums[mid])
        root.left = self.helper(nums[:mid])
        root.right = self.helper(nums[mid + 1:])
        return root
        
        
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return self.helper(nums)