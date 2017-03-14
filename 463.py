class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #Idea: Scan all lands and counts the total number of water-land boundaries.
        r = 0
        length = len(grid)
        width = len(grid[0])
        for i in range(length):
        	for j in range(width):
        		if grid[i][j] == 1:
        			if i == 0:
        				r += 1
        			elif grid[i - 1][j] == 0:
        				r += 1
        			if i == length - 1:
        				r += 1
        			elif grid[i + 1][j] == 0:
        				r += 1
        			if j == 0:
        				r += 1
        			elif grid[i][j - 1] == 0:
        				r += 1
        			if j == width - 1:
        				r += 1
        			elif grid[i][j + 1] == 0:
        				r += 1
        return r

s = Solution()
print s.islandPerimeter([[0,1,0,0], [1,1,1,0], [0,1,0,0], [1,1,0,0]])