class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        res = [0] * len(matrix) * len(matrix[0])
        i, j = 0, 0
        visited = {}
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] #(0, 1)->right, (1, 0)->down, (0, -1)->left, (-1, 0)->up
        curDirection = 0
        for k in xrange(len(matrix) * len(matrix[0])):
            res[k] = matrix[i][j]
            visited[(i, j)] = 1
            i += directions[curDirection][0]
            j += directions[curDirection][1]
            if i < 0 or i > len(matrix) - 1 or j < 0 or j > len(matrix[0]) - 1 or (i, j) in visited:
                i -= directions[curDirection][0]
                j -= directions[curDirection][1]
                curDirection = (curDirection + 1) % 4
                i += directions[curDirection][0]
                j += directions[curDirection][1]
        return res

s = Solution()
print s.spiralOrder([])
        	