class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        while low < high - 1:
            mid = low + (high - low) / 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                low = mid
            else:
                high = mid
        if nums[low] < target:
            if nums[high] < target:
                return high + 1
            return low + 1
        else:
            return low