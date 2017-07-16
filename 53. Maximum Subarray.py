class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sub_sum = 0
        res = nums[0]
        for num in nums:
            sub_sum += num
            if sub_sum > res:
                res = sub_sum
            if sub_sum < 0:
                sub_sum = 0
        return res