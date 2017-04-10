class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num:
        	if num % 9:
        		return num % 9
        	else:
        		return 9
        else:
        	return 0