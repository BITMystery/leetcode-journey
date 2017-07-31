# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    index = {None: 0}
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            self.index[root] = root.val
            return root.val
        res1 = self.rob(root.left) + self.rob(root.right)
        res2 = root.val
        if root.left:
            res2 += self.index[root.left.left] + self.index[root.left.right]
        if root.right:
            res2 += self.index[root.right.left] + self.index[root.right.right]
        self.index[root] = max(res1, res2)
        return max(res1, res2)