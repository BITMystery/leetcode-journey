class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        counter = 0
        n = num
        while(num):
        	num /= 2
        	counter += 1
        r = n ^ (2 ** counter - 1)
        return r

s = Solution()
print s.findComplement(5)
