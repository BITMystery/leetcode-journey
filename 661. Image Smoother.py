class Solution(object):
    def get_average(self, i, j, row, col, M):
        res = 0
        counter = 0
        for x in xrange(-1, 2):
            for y in xrange(-1, 2):
                if not (i + x < 0 or i + x >= row or j + y < 0 or j + y >= col):
                    res += M[i + x][j + y]
                    counter += 1
        return res / counter


    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(M)
        col = len(M[0])
        res = [[0 for _ in xrange(col)] for _ in xrange(row)]
        for i in xrange(row):
            for j in xrange(col):
                res[i][j] = self.get_average(i, j, row, col, M)
        return res