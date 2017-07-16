class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #No notation. Return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]
        low = 0
        high = len(nums) - 1
        while low < high - 1:
            mid = low + (high - low) / 2
            if nums[mid] > nums[0]:
                low = mid
            else:
                high = mid
        return min(nums[low], nums[high])