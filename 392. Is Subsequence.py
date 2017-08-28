class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        start = 0
        for letter in s:
            p = t[start:].find(letter)
            if p == -1:
                return False
            start += p + 1
        return True

class Solution_2(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        it = iter(t)
        return all(letter in it for letter in s)