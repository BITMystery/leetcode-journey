# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def delete_root(self, root):
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        node = root.left
        while node.right:
            node = node.right
        node.right = root.right
        return root.left
    
        
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None
        node = root
        pre_node = root
        while node:
            if node.val < key:
                pre_node = node
                node = node.right
            elif node.val > key:
                pre_node = node
                node = node.left
            else:
                if pre_node.val < key:
                    pre_node.right = self.delete_root(node)
                    return root
                if pre_node.val > key:
                    pre_node.left = self.delete_root(node)
                    return root
                else:
                    return self.delete_root(node)
        return root
                        