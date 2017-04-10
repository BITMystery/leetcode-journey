# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderWalk(self, node, total):
    	if not node:
    		return total
    	total = self.inorderWalk(node.right, total)
    	total += node.val
    	node.val = total
    	total = self.inorderWalk(node.left, total)
    	return total
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.inorderWalk(root, 0)
        return root

s = Solution()
root = TreeNode(2)
root.right = TreeNode(3)
root.left = TreeNode(1)
s.convertBST(root)
print root.val, root.left.val, root.right.val