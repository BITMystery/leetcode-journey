class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_num = min(nums)
        r = 0
        for num in nums:
        	r += num - min_num
        return r

s = Solution()
print s.minMoves([1,2,3])