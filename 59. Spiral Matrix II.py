class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        for k in xrange(n):
        	res.append([0] * n)
        i, j = 0, 0
        count = 1
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] #(0, 1)->right, (1, 0)->down, (0, -1)->left, (-1, 0)->up
        curDirection = 0
        for k in xrange(n*n):
        	res[i][j] = count
        	count += 1
        	i += directions[curDirection][0]
        	j += directions[curDirection][1]
        	if i < 0 or i > n - 1 or j < 0 or j > n - 1 or res[i][j] != 0:
        		i -= directions[curDirection][0]
        		j -= directions[curDirection][1]
        		curDirection = (curDirection + 1) % 4
        		i += directions[curDirection][0]
        		j += directions[curDirection][1]
        return res

s = Solution()
print s.generateMatrix(0)
        	