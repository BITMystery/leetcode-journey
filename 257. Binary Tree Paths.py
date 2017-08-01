# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root, path, res):
        if not root:
            return
        if not root.left and not root.right:
            if path:
                res.append(path + '->' + str(root.val))
            else:
                res.append(str(root.val))
        if path:
            self.helper(root.left, path + '->' + str(root.val), res)
            self.helper(root.right, path + '->' + str(root.val), res)
        else:
            self.helper(root.left, str(root.val), res)
            self.helper(root.right, str(root.val), res)
        
        
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        res = []
        self.helper(root, '', res)
        return res