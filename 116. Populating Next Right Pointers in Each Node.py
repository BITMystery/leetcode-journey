# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        stack = [root]
        while stack:
            temp_stack = []
            for node in stack:
                if node.right:
                    temp_stack.append(node.right)
                if node.left:
                    temp_stack.append(node.left)
            while stack:
                node = stack.pop()
                node.next = None if not stack else stack[-1]
            stack = temp_stack