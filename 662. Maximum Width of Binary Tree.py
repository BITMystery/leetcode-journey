# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        root.val = 1
        level = [root]
        res = 0
        while level:
            width = level[-1].val - level[0].val + 1
            res = max(res, width)
            next_level = []
            for node in level:
                if node.left:
                    node.left.val = node.val * 2
                    next_level.append(node.left)
                if node.right:
                    node.right.val = node.val * 2 + 1
                    next_level.append(node.right)
            del level
            level = next_level
        return res