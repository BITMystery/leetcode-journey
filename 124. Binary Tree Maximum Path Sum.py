# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    max_path_sum = None
    def helper(self, root):
        if not root:
            return 0
        max_left_sum = self.helper(root.left)
        max_right_sum = self.helper(root.right)
        max_root_sum = root.val + max(0, max_left_sum, max_right_sum, max_left_sum + max_right_sum)
        self.max_path_sum = max(self.max_path_sum, max_root_sum)
        return root.val + max(0, max_left_sum, max_right_sum)
        
    
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.helper(root)
        return self.max_path_sum