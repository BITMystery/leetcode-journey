class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 10 ** n - int((5 * n * n - 6 * n + 1) * 10 ** (n-2))

s = Solution()
print s.countNumbersWithUniqueDigits(2)