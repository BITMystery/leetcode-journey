class Solution(object):    
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # dp = [[1, 1, ..., 1]
        #       [0, ?, ..., ?]
        #       [0,    ...   ]
        #       [0, ?, ..., ?]]
        dp = [[0 for _ in xrange(len(s) + 1)] for _ in xrange(len(t) + 1)]
        for i in xrange(len(s) + 1):
            dp[0][i] = 1
        for i in xrange(1, len(t) + 1):
            for j in xrange(1, len(s) + 1):
                if s[j - 1] == t[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        return dp[-1][-1]