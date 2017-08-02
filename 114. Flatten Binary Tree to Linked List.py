# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root):
        if not root:
            return None, None
        left_head, left_tail = self.helper(root.left)
        right_head, right_tail = self.helper(root.right)
        if not left_head:
            if not right_head:
                return root, root
            else:
                return root, right_tail
        else:
            root.right = left_head
            root.left = None
            if not right_head:
                return root, left_tail
            else:
                left_tail.right = right_head
                return root, right_tail
        
        
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.helper(root)
        