class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = {}
        for num in nums:
        	tmp = index[num] = index.get(num, 0) + 1
        	if tmp > len(nums) / 2:
        		return num

s = Solution()
print s.majorityElement([1])