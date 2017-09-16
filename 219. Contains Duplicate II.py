class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) == 0 or k <= 0:
            return False
        if k + 1 >= len(nums):
            return len(set(nums)) < len(nums)
        s = set(nums[0:k + 1])
        if k + 1 > len(s):
            return True
        for i in xrange(len(nums) - k - 1):
            s.remove(nums[i])
            s.add(nums[i + k + 1])
            if k + 1 > len(s):
                return True
        return False