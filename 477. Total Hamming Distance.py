class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        flag = 1
        while flag:
        	flag = num_zero = num_one = 0
        	for i in xrange(len(nums)):
        		if nums[i] & 1 == 1:
        			num_one += 1
        		else:
        			num_zero += 1
        		nums[i] >>= 1
        		if nums[i]:
        			flag = 1
        	res += num_zero * num_one
        return res

s = Solution()
print s.totalHammingDistance([0, 0, 1])