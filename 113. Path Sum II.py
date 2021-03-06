# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root, sum, path, res):
        if not root:
            return
        if not root.left and not root.right and root.val == sum:
            res.append(path + [root.val])
        self.helper(root.left, sum - root.val, path + [root.val], res)
        self.helper(root.right, sum - root.val, path + [root.val], res)
        
        
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        self.helper(root, sum, [], res)
        return res