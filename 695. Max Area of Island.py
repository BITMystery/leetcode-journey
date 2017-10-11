class Solution(object):
    def island_area(self, grid, row, col):
        area = 0
        stack = [(row, col)]
        grid[row][col] = -1
        while stack:
            new_stack = []
            while stack:
                i, j = stack.pop()
                area += 1
                grid[i][j] = -1
                if i - 1 >= 0 and grid[i - 1][j] == 1:
                    new_stack.append((i - 1, j))
                    grid[i - 1][j] = -1
                if i + 1 < len(grid) and grid[i + 1][j] == 1:
                    new_stack.append((i + 1, j))
                    grid[i + 1][j] = -1
                if j - 1 >= 0 and grid[i][j - 1] == 1:
                    new_stack.append((i, j - 1))
                    grid[i][j - 1] = -1
                if j + 1 < len(grid[0]) and grid[i][j + 1] == 1:
                    new_stack.append((i, j + 1))
                    grid[i][j + 1] = -1
            stack = new_stack
        return area
        
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_area = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == 1:
                    area = self.island_area(grid, i, j)
                    max_area = max(max_area, area)
        return max_area