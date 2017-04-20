import collections

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = collections.Counter(s)
        for i in xrange(len(s)):
        	if d[s[i]] == 1:
        		return i
        return -1

s = Solution()
print s.firstUniqChar("")