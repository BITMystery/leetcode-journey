# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root, index):
        if not root:
            return 'X'
        res = str(root.val)
        res += '(' + self.helper(root.left, index) + ',' + self.helper(root.right, index) + ')'
        if res not in index:
            index[res] = [root, 1]
        else:
            index[res][1] += 1
        return res
        
        
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        res = []
        index = {}
        self.helper(root, index)
        for key in index.keys():
            if index[key][1] > 1:
                res.append(index[key][0])
        return res