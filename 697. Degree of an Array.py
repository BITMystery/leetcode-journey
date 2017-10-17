from collections import Counter


class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = Counter(nums)
        degree = max(c.values())
        if degree == 1:
            return 1
        ends = {}
        for i, num in enumerate(nums):
            if c[num] == degree:
                if num not in ends:
                    ends[num] = [i, None]
                else:
                    ends[num][1] = i
        return min([right - left + 1 for [left, right] in ends.values()])
                