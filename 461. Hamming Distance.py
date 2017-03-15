class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        r = 0
        if x < y:
            temp = y
            y = x
            x = temp
        while(x != 0):
            last_bit_x = x % 2
            last_bit_y = y % 2
            x /= 2
            y /= 2
            if last_bit_x != last_bit_y:
                r += 1
        return r
