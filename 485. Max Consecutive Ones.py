class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_of_onces = 0
        r = 0
        for num in nums:
        	if num:
        		num_of_onces += 1
        	else:
        		if num_of_onces > r:
        			r = num_of_onces
        		num_of_onces = 0
        if num_of_onces > r:
        		r = num_of_onces
        return r

s = Solution()
print s.findMaxConsecutiveOnes([1,1,1,1])