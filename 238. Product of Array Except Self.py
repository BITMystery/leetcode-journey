class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p = 1
        r = [0] * len(nums)
        for i in xrange(len(nums)):
        	r[i] = p
        	p *= nums[i]
        p = 1
        for i in xrange(len(nums) - 1, -1, -1):
        	r[i] *= p
        	p *= nums[i]
        return r

s = Solution()
print s.productExceptSelf([1,2,3,4])