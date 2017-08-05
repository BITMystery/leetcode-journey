# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def height(self, root):
        if not root:
            return 0
        return 1 + self.height(root.left)
    
    
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        h = self.height(root)
        if h == 0:
            return 0
        if h == 1:
            return 1
        if self.height(root.right) == h - 1:
            return 2 ** (h - 1) + self.countNodes(root.right)
        else:
            return 2 ** (h - 2) + self.countNodes(root.left)