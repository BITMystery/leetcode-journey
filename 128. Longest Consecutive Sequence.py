class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        index = {}
        for v in nums:
            if v in index:
                continue
            left = index.get(v - 1, 0)
            right = index.get(v + 1, 0)
            index[v - left] = left + right + 1
            index[v + right] = left + right + 1
            index[v] = left + right + 1
            res = max(res, left + right + 1)
        return res