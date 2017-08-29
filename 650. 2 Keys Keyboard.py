class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        prime_nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31] # note n <= 1000
        for factor in prime_nums:
            if n % factor == 0:
                return factor + self.minSteps(n / factor)
        return n