# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = [root]
        while stack:
            temp_stack = []
            for node in stack:
                if node:
                    temp_stack.append(None if not node.left else node.left)
                    temp_stack.append(None if not node.right else node.right)
            values = [node.val if node else None for node in temp_stack]
            if values[:len(temp_stack) / 2] != values[:len(temp_stack) / 2 - 1:-1]:
                return False
            stack = temp_stack
        return True