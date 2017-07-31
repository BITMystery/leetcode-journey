# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root, d, res):
        if not root:
            return
        if d > len(res):
            res.append(root.val)
            t = d
        self.helper(root.right, d + 1, res)
        self.helper(root.left, d + 1, res)
            
        
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.helper(root, 1, res)
        return res