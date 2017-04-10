# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
        	return None
        if root.left != None or root.right != None:
        	self.invertTree(root.left)
        	self.invertTree(root.right)
        	temp = root.left
        	root.left = root.right
        	root.right = temp
        return root

s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = None
s.invertTree(root)
print root.right.val