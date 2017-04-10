# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    min_dif = None
    last_visited = None
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
        	return None
        self.getMinimumDifference(root.left)
        if self.last_visited == None:
        	self.last_visited = root.val
        else:
        	dif = root.val - self.last_visited
        	if self.min_dif == None or self.min_dif > dif:
        		self.min_dif = dif
        	self.last_visited = root.val
        self.getMinimumDifference(root.right)
        return self.min_dif

s = Solution()
root = TreeNode(0)
root.right = TreeNode(2236)
root.right.left = TreeNode(1277)
root.right.right = TreeNode(2776)
root.right.left.left = TreeNode(519)
print s.getMinimumDifference(root)