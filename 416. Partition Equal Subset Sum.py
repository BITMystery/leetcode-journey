class Solution(object):
    def helper(self, nums, start, s, target):
        if s == target:
            return True
        for i in xrange(start, len(nums) - 1):
            if s + nums[i] > target:
                continue
            if self.helper(nums, i + 1, s + nums[i], target):
                return True
        return False
        
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return False
        s = sum(nums)
        if s % 2 == 1:
            return False
        nums.sort(reverse = True)
        if nums[0] > s / 2:
            return False
        if nums[0] == s / 2:
            return True
        return self.helper(nums, 0, 0, s / 2)