# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        res = ''
        stack = [root]
        while stack:
            node = stack.pop()
            res += str(node.val) + ' '
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        print res[:-1]
        return res[:-1]
        
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        values = data.split()
        if not values:
            return None
        root = TreeNode(int(values[0]))
        for value in values[1:]:
            value = int(value)
            node = root
            while node:
                if value < node.val:
                    if node.left:
                        node = node.left
                    else:
                        node.left = TreeNode(value)
                        break
                else:
                    if node.right:
                        node = node.right
                    else:
                        node.right = TreeNode(value)
                        break
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
