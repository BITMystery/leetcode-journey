# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        if not root:
        	return 0
        if root.left:
        	if root.left.left != None or root.left.right != None:
        		res += self.sumOfLeftLeaves(root.left)
        	else:
        		res += root.left.val
        if root.right:
        	if root.right.left != None or root.right.right != None:
        		res += self.sumOfLeftLeaves(root.right)
        return res