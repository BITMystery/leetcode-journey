class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
        	return []
        i = 1
        j = -1
        row = len(matrix)
        col = len(matrix[0])
        res = [0] * row * col
        direction = 1 # 1: top-right, 0: bottom-left
        counter = 0
        while counter < row * col:
        	if direction:
        		i -= 1
        		j += 1
        		if i < 0 or j > col - 1:
        			i += 1
        			if j > col - 1:
        				i += 1
        				j -= 1
        			direction = 0
        	else:
        		i += 1
        		j -= 1
        		if i > row -1 or j < 0:
        			j += 1
        			if i > row - 1:
        				i -= 1
        				j += 1
        			direction = 1
        	res[counter] = matrix[i][j]
        	counter += 1
        return res

s = Solution()
print s.findDiagonalOrder([[1, 4, 7]])