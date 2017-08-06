# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        stack = []
        cur = root
        prev_val = None
        while stack or cur:
            if cur:
                node = stack.append(cur)
                cur = cur.left
                continue
            cur = stack.pop()
            cur_val = cur.val
            if prev_val >= cur_val:
                return False
            prev_val = cur_val
            cur = cur.right
        return True