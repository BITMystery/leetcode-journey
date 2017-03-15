class Solution(object):
    def isCapital(self, l):
        if 'A' <= l <= 'Z':
    	    return True
        else:
    	    return False
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if 'A' <= word[0] <= 'Z':
        	if 0 < len(filter(self.isCapital, word[1:])) < len(word[1:]):
        		return False
        else:
        	if len(filter(self.isCapital, word[1:])) > 0:
        		return False
        return True

class Solution_2(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        #Using built-in functions
        return word.isupper() or word.islower() or word.istitle()

s = Solution_2()
print s.detectCapitalUse('FlaG')
