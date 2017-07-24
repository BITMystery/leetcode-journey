class Solution(object):       
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in xrange(0, len(s)):
            for j in xrange(i + 1, len(s) + 1):
                if s[i:j] == s[i:j][::-1]:
                    res += 1
        return res