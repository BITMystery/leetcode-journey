import sys

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack = []
        minSecondNum = sys.maxint
        for num in nums:
        	if num > minSecondNum:
        		return True
        	if not stack:
        		stack.append(num)
        	else:
        		if num > stack[-1]:
        			stack.append(num)
        			if len(stack) == 3:
        				return True
        		else:
        			tmp = stack.pop()
        			if len(stack) == 1:
        				if num <= stack[-1]:
        					stack.pop()
        				if tmp < minSecondNum:
        					minSecondNum = tmp
        			stack.append(num)
        return False

s = Solution()
print s.increasingTriplet([4, 2, 1, 3, 2, 1, 5])