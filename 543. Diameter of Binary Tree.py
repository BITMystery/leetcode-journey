# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    diameter = 0
    
    
    def helper(self, root):
        if not root:
            return 0, 0
        l = max(self.helper(root.left))
        r = max(self.helper(root.right))
        d = l + r
        self.diameter = max(self.diameter, d)
        return 1 + l, 1 + r
        
        
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.helper(root)
        return self.diameter
