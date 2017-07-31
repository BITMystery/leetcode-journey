# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root, level, res):
        if not root:
            return
        if level == len(res):
            res.append([root.val])
        else:
            res[level].append(root.val)
        self.helper(root.left, level + 1, res)
        self.helper(root.right, level + 1, res)
        
        
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.helper(root, 0, res)
        return res