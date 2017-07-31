class Solution(object):
    index = {0: 1, 1: 1}
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 1
        res = 0
        i = 0
        while i < n:
            x = self.index[i] if i in self.index else self.numTrees(i)
            y = self.index[n - 1 - i] if n - 1 - i in self.index else self.numTrees(n - 1- i)
            res += x * y
            i += 1
        self.index[n] = res
        return res