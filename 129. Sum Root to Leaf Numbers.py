# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root, path):
        if not root:
            return 0
        res = 0
        if not root.left and not root.right:
            return int(str(path + str(root.val)))
        res += self.helper(root.left, path + str(root.val))
        res += self.helper(root.right, path + str(root.val))
        return res
    
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root, '')