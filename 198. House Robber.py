class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        #rob: max money after robbing last house
        #skip: max money after skipping last house
        rob, skip, rob_pre = nums[0], 0, 0 # initial state
        
        for i in xrange(1, len(nums)):
            cur_rob = skip + nums[i]
            cur_skip = max(skip, rob)
            rob, skip = cur_rob, cur_skip
        
        return max(rob, skip)