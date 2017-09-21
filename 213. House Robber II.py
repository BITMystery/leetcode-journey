class Solution(object):
    def rob_no_circle(self, nums):
        rob_last, not_rob_last = nums[0], 0
        for num in nums[1:]:
            rob_this = not_rob_last + num
            not_rob_this = max(rob_last, not_rob_last)
            rob_last, not_rob_last = rob_this, not_rob_this
        return max(rob_last, not_rob_last)
            
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) <= 3:
            return max(nums)
        # max money if rob the 1st house
        rob_first = nums[0] + self.rob_no_circle(nums[2: -1])
        # max money if not rob the 1st house
        not_rob_first = self.rob_no_circle(nums[1:])
        return max(rob_first, not_rob_first)