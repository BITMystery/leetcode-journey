class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = 0
        for num in nums:
        	r = r ^ num
        return r

s = Solution()
print s.singleNumber([1,3,3,2,2])