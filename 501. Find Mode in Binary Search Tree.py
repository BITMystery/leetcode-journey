# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        stack = []
        while root:
            stack.append(root)
            root = root.left
        pre_val = None
        max_num = 1
        counter = 1
        while stack:
            node = stack.pop()
            cur_val = node.val
            if cur_val == pre_val:
                counter += 1
                if counter == max_num:
                    res.append(cur_val)
                elif counter > max_num:
                    max_num = counter
                    del res
                    res = [cur_val]
            else:
                counter = 1
                pre_val = cur_val
                if counter == max_num:
                    res.append(cur_val)
            node = node.right
            while node:
                stack.append(node)
                node = node.left
        return res
            
                    
        