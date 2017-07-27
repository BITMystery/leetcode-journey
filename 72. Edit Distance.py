class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if word1 == '' or word2 == '':
            return abs(len(word1) - len(word2))
        dp = [[0 for _ in xrange(len(word1) + 1)] for _ in xrange(len(word2) + 1)] # O(mn) space. Can be improve to O(min(m, n))
        for i in xrange(len(word1) + 1):
            dp[0][i] = i
        for i in xrange(len(word2) + 1):
            dp[i][0] = i
        for i in xrange(1, len(word2) + 1):
            for j in xrange(1, len(word1) + 1):
                if word1[j - 1] == word2[i - 1]:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1] + 1, dp[i - 1][j] + 1)
                else:
                    dp[i][j] = min(dp[i - 1][j - 1] + 1, dp[i][j - 1] + 1, dp[i - 1][j] + 1)
        return dp[-1][-1]