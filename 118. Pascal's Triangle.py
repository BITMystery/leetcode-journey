class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        t = [[1]]
        for i in xrange(1, numRows):
            new_row = []
            # generate the row
            for j in xrange(i / 2 + 1):
                # t[i][j] = t[i - 1][j - 1] + t[i - 1][j]
                if j - 1 < 0:
                    new_row.append(t[i - 1][j])
                else:
                    new_row.append(t[i - 1][j - 1] + t[i - 1][j])
            if i % 2 != 0:
                t.append(new_row + list(reversed(new_row)))
            else:
                t.append(new_row + list(reversed(new_row[: len(new_row) - 1])))
        return t