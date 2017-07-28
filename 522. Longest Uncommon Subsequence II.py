class Solution(object):
    def is_subsequence(self, s, t):
        # always suppose len(s) <= len(t)
        if s == '' or s == t:
            return True
        elif len(s) == len(t):
            return False
        else:
            i = 0
            for j in xrange(len(t)):
                if t[j] == s[i]:
                    i += 1
                    if i == len(s):
                        return True
            return False
        
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        res = 0
        strs.sort(key = len, reverse = True)
        for i in xrange(len(strs)):
            res = len(strs[i])
            for j in xrange(len(strs)):
                if i == j:
                    continue
                if len(strs[i]) > len(strs[j]):
                    break
                if self.is_subsequence(strs[i], strs[j]):
                    res = 0
            if res:
                break
        return res if res else -1