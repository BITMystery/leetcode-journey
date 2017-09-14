class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones = zeroes = 0
        index = {0: -1}
        res = 0
        for i in xrange(len(nums)):
            if nums[i] == 0:
                zeroes += 1
            else:
                ones += 1
            if zeroes - ones in index:
                l = i - index[zeroes - ones]
                res = max(res, l)
            else:
                index[zeroes - ones] = i
        return res