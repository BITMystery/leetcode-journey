class Solution(object):        
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        res = []
        while root:
            stack.append(root)
            root = root.left
        while stack:
            node = stack.pop()
            res.append(node.val)
            node = node.right
            while node:
                stack.append(node)
                node = node.left
        return res
