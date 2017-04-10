class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = 0
        i = 0
        while i < len(nums):
        	if not nums[i]:
        		nums.pop(i)
        		count += 1
        		i -= 1
        	i += 1
        for i in xrange(count):
        	nums.append(0)

s = Solution()
nums = [0, 0, 0, 1, 0]
s.moveZeroes(nums)
print nums