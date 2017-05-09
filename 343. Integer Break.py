class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
        	return 1
        if n == 3:
        	return 2
        if n == 4:
        	return 4
        res = 1
        while n > 4:
        	res *= 3
        	n -= 3
        res *= n
        return res

s = Solution()
for i in xrange(2, 58):
	print s.integerBreak(i)