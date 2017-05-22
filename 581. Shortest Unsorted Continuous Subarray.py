class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = len(nums)
        end = -1
        cur_max = -10000
        for i in xrange(len(nums) - 1):
        	if nums[i] > nums[i+1]:
        		j = i
        		while j - 1 >= 0:
        			if nums[j-1] > nums[i+1]:
        				j -= 1
        				continue
        			break
        		start = min(j, start)
        		end = i + 1
        		cur_max = max(nums[i], cur_max)
        	elif start != len(nums) and cur_max > nums[i+1]:
        		end = i + 1
        if start == len(nums):
        	return 0
        else:
        	print start, end
        	return end - start + 1


s = Solution()
print s.findUnsortedSubarray([1,5,3,2,4])