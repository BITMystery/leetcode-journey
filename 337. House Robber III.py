# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root):
        if not root:
            return 0, 0
        rob_left, not_rob_left = self.helper(root.left)
        rob_right, not_rob_right = self.helper(root.right)
        rob_root = root.val + not_rob_left + not_rob_right
        not_rob_root = max(rob_left, not_rob_left) + max(rob_right, not_rob_right)
        return rob_root, not_rob_root
        
        
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.helper(root))
