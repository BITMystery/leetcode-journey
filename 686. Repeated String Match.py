class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        len_a, len_b = len(A), len(B)
        for i in xrange(1, len_b/len_a + 3):
            if B in A * i:
                return i
        return -1