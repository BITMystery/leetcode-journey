class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if None == nums or len(nums) == 0:
            return []
        if len(nums) == 1:
            return [[], [nums[0]]]
        res = self.subsets(nums[1:])
        l = len(res)
        for i in xrange(l):
            res.append([nums[0]] + res[i])
        return res