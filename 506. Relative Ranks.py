class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        sorted_nums = sorted(nums, reverse = True)
        d = {}
        for i in xrange(len(sorted_nums)):
        	d[sorted_nums[i]] = str(i + 1)
        for i in xrange(len(nums)):
        	rank = d[nums[i]]
        	if rank == '1':
        		nums[i] = 'Gold Medal'
        	elif rank == '2':
        		nums[i] = 'Silver Medal'
        	elif rank == '3':
        		nums[i] = 'Bronze Medal'
        	else:
        		nums[i] = rank
        return nums

s = Solution()
print s.findRelativeRanks([5, 3, 7, 1])