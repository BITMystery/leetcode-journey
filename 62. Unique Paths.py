class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # Res = C_{m+n-2}^{m-1}
        if m < 1 or n < 1:
            return 0
        numerator = 1
        denominator = 1
        if m > n:
            m, n = n, m
        for i in xrange(m - 1):
            numerator *= m + n - 2 - i
            denominator *= i + 1
        return numerator / denominator