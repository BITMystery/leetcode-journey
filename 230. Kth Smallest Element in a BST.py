# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        res = 0
        stack = []
        while root:
            stack.append(root)
            root = root.left
        for _ in xrange(k):
            node = stack.pop()
            res = node.val
            node = node.right
            while node:
                stack.append(node)
                node = node.left
        return res
