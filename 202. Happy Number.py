class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        history = set()
        while True:
            m = 0
            while n:
                m += (n % 10) ** 2
                n /= 10
            if m == 1:
                return True
            if m in history:
                return False
            history.add(m)
            n = m