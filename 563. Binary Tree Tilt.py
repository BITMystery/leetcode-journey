# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper1(self, root, index):
        # calculate the sum of a given tree
        if not root:
            return 0
        node_sum = root.val + self.helper1(root.left, index) + self.helper1(root.right, index)
        index[root] = node_sum
        return node_sum
    
    def helper2(self, root, index):
        # calculate the tilt of a given tree
        if not root:
            return 0
        res = abs(index[root.left] - index[root.right])
        res += self.helper2(root.left, index) + self.helper2(root.right, index)
        return res
        
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        index = {None: 0}
        self.helper1(root, index)
        return self.helper2(root, index)