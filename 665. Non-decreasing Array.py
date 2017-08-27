class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        chance = 1
        for i in xrange(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if not chance:
                    return False
                if i == 0 or nums[i - 1] <= nums[i + 1]:
                    nums[i] = nums[i + 1]
                else:
                    nums[i + 1] = nums[i]
                chance -= 1
        return True