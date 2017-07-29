# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import Counter

class Solution(object):
    def helper(self, root, sums):
        if None == root:
            return 0
        s = root.val
        s += self.helper(root.left, sums) + self.helper(root.right, sums)
        sums.append(s)
        return s
        
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if None == root:
            return []
        sums = []
        self.helper(root, sums)
        c = Counter(sums)
        max_freq = max([item[1] for item in c.items()])
        for item in c.items():
            if item[1] == max_freq:
                res.append(item[0])
        return res
