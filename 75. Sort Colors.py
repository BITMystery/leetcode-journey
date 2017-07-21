class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        red_num = white_num = blue_num = 0
        for num in nums:
            if num == 0:
                red_num += 1
            elif num == 1:
                white_num += 1
            else:
                blue_num += 1
        for i in xrange(len(nums)):
            if i < red_num:
                nums[i] = 0
            elif i < red_num + white_num:
                nums[i] = 1
            else:
                nums[i] = 2
        