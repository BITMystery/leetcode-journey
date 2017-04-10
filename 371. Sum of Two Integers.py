class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        s = str(10 ** a * 10 ** b / 10)
        if s[0]:
        	return len(s)
        else:
        	return -1 * len(s)

s = Solution()
print s.getSum(1, -2)