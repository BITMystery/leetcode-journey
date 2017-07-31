# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    visited = 0
    value = 0
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return
        if k == self.visited:
            return
        self.kthSmallest(root.left, k)
        self.visited += 1
        if k == self.visited:
            self.value = root.val
        self.kthSmallest(root.right, k)
        return self.value