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
            return 'X'
        if not root.left and not root.right:
            return str(root.val)
        l = self.serialize(root.left) if root.left else 'X'
        r = self.serialize(root.right) if root.right else 'X'
        return '%s(%s,%s)' % (str(root.val), l, r)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        i = data.find('(')
        if i == -1:
            if data == 'X':
                return None
            return TreeNode(int(data))
        else:
            root = TreeNode(int(data[:i]))
            j = i + 1
            stack = []
            while data[j] != ',' or stack != []:
                if data[j] == '(':
                    stack.append(1)
                elif data[j] == ')':
                    stack.pop()
                j += 1
            root.left = self.deserialize(data[i + 1:j])
            root.right = self.deserialize(data[j + 1: -1])
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))