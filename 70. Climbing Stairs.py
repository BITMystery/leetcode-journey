class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        pre = 2
        pre_pre = 1
        for step in xrange(3, n + 1):
            cur = pre + pre_pre
            pre_pre = pre
            pre = cur
        return pre