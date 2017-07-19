class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if i - 1 < 0 and j - 1 < 0:
                    continue
                elif i - 1 < 0:
                    grid[i][j] += grid[i][j - 1]
                elif j - 1 < 0:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]