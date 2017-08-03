# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        root = TreeNode(postorder[-1])
        i = inorder.index(postorder[-1])
        left_inorder = inorder[:i]
        right_inorder = inorder[i + 1:]
        left_postorder = postorder[:i]
        right_postorder = postorder[i:-1]
        root.left = self.buildTree(left_inorder, left_postorder)
        root.right = self.buildTree(right_inorder, right_postorder)
        return root