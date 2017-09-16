class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) <= 10:
            return []
        seen = set()
        res = set()
        for i in xrange(len(s) - 10 + 1):
            if s[i:i + 10] not in seen:
                seen.add(s[i:i + 10])
            else:
                res.add(s[i:i + 10])
        return list(res)