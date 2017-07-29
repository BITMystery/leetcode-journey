from collections import Counter
class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if Counter(s1) != Counter(s2):
            return False
        if len(s1) < 2:
            return True
        c1 = Counter()
        c2 = Counter()
        c3 = Counter()
        for i in xrange(0, len(s1) - 1):
            c1 += Counter([s1[i]])
            c2 += Counter([s2[i]])
            c3 += Counter([s2[-1 - i]])
            if c1 == c2:
                if self.isScramble(s1[:i + 1], s2[:i + 1]) and self.isScramble(s1[i + 1:], s2[i + 1:]):
                    return True
            elif c1 == c3:
                if self.isScramble(s1[:i + 1], s2[-1 - i:]) and self.isScramble(s1[i + 1:], s2[:-1 - i]):
                    return True
        return False
                