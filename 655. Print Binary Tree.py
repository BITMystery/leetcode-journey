# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def get_height(self, root):
        if not root:
            return 0
        return 1 + max(self.get_height(root.left), self.get_height(root.right))
        
        
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        row = self.get_height(root)
        col = 2 ** row - 1
        res = []
        stack = [root]
        for i in xrange(row):
            line = []
            gap = 2 ** (row - i) - 1
            new_stack = []
            for j in xrange(len(stack)):
                line += [''] * ((gap + 1) / 2 - 1)
                node = stack[j]
                if not node:
                    new_stack.append(None)
                    new_stack.append(None)
                    line.append('')
                    if j != len(stack) - 1:
                        line += [''] * ((gap + 1) / 2)
                    else:
                        line += [''] * ((gap + 1) / 2 - 1)
                    continue
                if node.left:
                    new_stack.append(node.left)
                else:
                    new_stack.append(None)
                if node.right:
                    new_stack.append(node.right)
                else:
                    new_stack.append(None)
                line.append(str(node.val))
                if j != len(stack) - 1:
                    line += [''] * ((gap + 1) / 2)
                else:
                    line += [''] * ((gap + 1) / 2 - 1)
            res.append(line)
            del stack
            stack = new_stack
        return res