import collections

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        c = collections.Counter(s)
        l = c.items()
        l.sort(key = lambda x: x[1], reverse = True)
        r = ''
        for (char, frq) in l:
        	r += char * frq
        return r

s = Solution()
print s.frequencySort('')