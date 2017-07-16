class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        current_sum = res = sum(nums[:k])
        for i in xrange(len(nums) - k):
            #current_sum = sum(nums[i + 1: i + k + 1])
            current_sum = current_sum + nums[i + k] - nums[i]
            if current_sum > res:
                res = current_sum
        return float(res) / k