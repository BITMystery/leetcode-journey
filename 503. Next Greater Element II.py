class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        r = [None] * len(nums)
        for i in xrange(2*len(nums)-1):
        	for j in xrange(len(stack)-1, -1, -1):
        		if nums[i%len(nums)] > nums[stack[j]]:
        			r[stack[j]] = nums[i%len(nums)]
        			stack.pop()
        			continue
        		break
        	if r[i%len(nums)] == None:
        		stack.append(i%len(nums))
        for i in xrange(len(nums)):
        	if r[i] == None:
        		r[i] = -1
        return r

s = Solution()
print s.nextGreaterElements([3,7,8,2,5])