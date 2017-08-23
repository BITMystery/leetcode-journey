class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        max_area = 0
        dp = [0] * (len(matrix[0]) + 1) # pad an extra 0
        for i in xrange(len(matrix)):
            stack = []
            for j in xrange(len(matrix[0])):
                dp[j] = 1 + dp[j] if matrix[i][j] == '1' else 0
            j = 0
            while j < len(matrix[0]) + 1:
                if not stack or dp[stack[-1]] < dp[j]:
                    stack.append(j)
                    j += 1
                else:
                    height = dp[stack.pop()]
                    width = j if not stack else j - stack[-1] - 1
                    area = height * width
                    max_area = max(max_area, area)
        return max_area