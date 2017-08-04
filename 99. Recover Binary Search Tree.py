# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        cur = root
        prev = first = second = None      
        while cur:
            if not cur.left:
                if prev and prev.val > cur.val:
                    if not first:
                        first = prev
                        second = cur
                    else:
                        second = cur
                prev = cur
                cur = cur.right
            else:
                temp = cur.left
                while temp.right and temp.right != cur:
                    temp = temp.right
                if temp.right == None:
                    temp.right = cur
                    cur = cur.left
                else:
                    if prev and prev.val > cur.val:
                        if not first:
                            first = prev
                            second = cur
                        else:
                            second = cur
                    temp.right = None
                    prev = cur
                    cur = cur.right
        first.val, second.val = second.val, first.val