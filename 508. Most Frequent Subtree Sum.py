# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    index = {}
    def postorderWalk(self, node):
    	if not node:
    		return 0
    	left_sum = self.postorderWalk(node.left)
    	right_sum = self.postorderWalk(node.right)
    	node_sum = node.val + left_sum + right_sum
    	node.val = node_sum
    	self.index[node_sum] = self.index.get(node_sum, 0) + 1
    	return node_sum
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.postorderWalk(root)
        r = []
        max_num = 0
        for val in self.index:
        	num = self.index[val]
        	if num > max_num:
        		r = [val]
        		max_num = num
        	elif num == max_num:
        		r.append(val)
        return r

s = Solution()
root = TreeNode(1)
root.right = TreeNode(2)
root.left = TreeNode(-3)
print s.findFrequentTreeSum(root)