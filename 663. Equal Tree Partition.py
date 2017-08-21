# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root, sums):
        if not root:
            return 0
        root_sum = root.val + self.helper(root.left, sums) + self.helper(root.right, sums)
        if root_sum not in sums:
            sums[root_sum] = 1
        else:
            sums[root_sum] += 1
        return root_sum
        
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        sums = {}
        root_sum = self.helper(root, sums)
        if root_sum % 2 != 0:
            return False
        if root_sum == 0:
            return True if sums[0] > 1 else False
        return root_sum / 2 in sums