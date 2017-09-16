class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        index = {}
        used = set()
        for i in xrange(len(s)):
            if s[i] in index:
                if index[s[i]] != t[i]:
                    return False
            else:
                if t[i] in used:
                    return False
                index[s[i]] = t[i]
                used.add(t[i])
        return True