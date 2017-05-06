import collections

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return collections.Counter(s) == collections.Counter(t)

s = Solution()
print s.isAnagram('abba', 'abcb')