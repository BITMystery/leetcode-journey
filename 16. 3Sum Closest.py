class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = float('inf')
        nums.sort()
        for i in xrange(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                if abs(target - nums[left] - nums[right] - nums[i]) > abs(target - res):
                    if target > nums[left] + nums[right] + nums[i]:
                        left += 1
                    else:
                        right -= 1
                else:
                    res = nums[left] + nums[right] + nums[i]
                    if target > res:
                        left += 1
                    elif target < res:
                        right -= 1
                    else:
                        return res
        return res