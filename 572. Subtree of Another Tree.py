# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def encode(self, root):
        if not root:
            return 'X'
        return '$%s(%s,%s)' % (str(root.val), self.encode(root.left), self.encode(root.right))
        
        
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        enc_s = self.encode(s)
        enc_t = self.encode(t)
        return enc_t in enc_s