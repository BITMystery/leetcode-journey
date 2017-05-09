class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
        	return '0'
        negtive = 0
        if num < 0:
        	negtive = 1
        	num = -num
        base = 7
        x = 1
        digits = []
        while x <= num:
        	x *= base
        x /= base
        while x:
        	digit = num / x
        	num %= x
        	digits.append(str(digit))
        	x /= base
        if negtive:
        	return '-' + ''.join(digits)
        else:
        	return ''.join(digits)

class Solution_2(object):
    def convertToBase7(self, num):
    	#Simplified
    	if num == 0:
    		return '0'
    	n = abs(num)
    	res = ''
    	base = 7
    	while n:
    		res = str(n % base) + res
    		n /= base
    	return res if num > 0 else '-' + res

s = Solution_2()
for i in xrange(-100, 100):
	print s.convertToBase7(i)