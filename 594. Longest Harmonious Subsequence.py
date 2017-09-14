from collections import Counter

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = Counter(nums)
        res = 0
        for num in nums:
            if c[num + 1]:
                res = max(res, c[num] + c[num + 1])
        return res