# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False
        stack = []
        while root:
            stack.append(root)
            root = root.left
        nums = []
        while stack:
            node = stack.pop()
            nums.append(node.val)
            node = node.right
            while node:
                stack.append(node)
                node = node.left
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == k:
                return True
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                right -= 1
        return False
        