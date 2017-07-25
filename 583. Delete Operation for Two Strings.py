class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[0 for _ in xrange(len(word2) + 1)] for _ in xrange(len(word1) + 1)]
        for i in xrange(1, len(word1) + 1):
            for j in xrange(1, len(word2) + 1):
                dp[i][j] = dp[i - 1][j - 1] + 1 if word1[i - 1] == word2[j - 1] else max(dp[i - 1][j], dp[i][j - 1])
        return len(word1) + len(word2) - 2 * dp[-1][-1]