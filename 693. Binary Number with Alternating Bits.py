class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        last_bit = n % 2
        while n:
            last_bit ^= 1
            n >>= 1
            if n % 2 != last_bit:
                return False
        return True