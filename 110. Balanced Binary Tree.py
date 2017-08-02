# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    balance = True
    
    
    def helper(self, root):
        if not root:
            return 0
        if not self.balance:
            return 0
        left_depth = self.helper(root.left)
        if not self.balance:
            return 0
        right_depth = self.helper(root.right)
        if abs(left_depth - right_depth) > 1:
            self.balance = False
        return max(left_depth, right_depth) + 1
        
        
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.helper(root)
        return self.balance