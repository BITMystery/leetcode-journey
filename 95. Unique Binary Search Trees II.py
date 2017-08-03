# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, n, start):
        if not n:
            return [None]
        res = []
        for i in xrange(start, start + n):
            l = self.helper(i - start, start)
            r = self.helper(n + start - i - 1, i + 1)
            for left_root in l:
                for right_root in r:
                    root = TreeNode(i)
                    root.left = left_root
                    root.right = right_root
                    res.append(root)
        return res
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if not n:
            return []
        return self.helper(n, 1)