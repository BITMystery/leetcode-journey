class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 0:
            return []
        res = [1] + [0] * rowIndex
        for i in xrange(rowIndex):
            before = 1
            for j in xrange(1, i + 2):
                res[j] += before
                before = res[j] - before
        return res