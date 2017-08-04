# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):    
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        pre_set = set()
        in_set = set()
        pos_set = set()
        stack = [root]
        while stack:
            node = stack.pop()
            pre_set.add(node)
            if node == p or node == q:
                break
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        stack = []
        node = root
        while node:
            stack.append(node)
            node = node.left
        counter = 0
        while stack:
            node = stack.pop()
            if node == p or node == q:
                counter += 1
            if counter == 1:
                in_set.add(node)
            elif counter == 2:
                in_set.add(node)
                break
            node = node.right
            while node:
                stack.append(node)
                node = node.left
        stack = [root]
        while stack:
            node = stack.pop()
            pos_set.add(node)
            if node == p or node == q:
                break
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return list(pre_set & in_set & pos_set)[0]
        