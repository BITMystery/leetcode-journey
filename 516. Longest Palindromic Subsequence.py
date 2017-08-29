class Solution(object):# O(n^2) time in worst case.
    def helper(self, s, start, end, mem):
        if start == end:
            return 1
        if start > end:
            return 0
        if s[start] == s[end]:
            if mem[start + 1][end - 1]:
                res = mem[start + 1][end - 1] + 2
            else:
                res = self.helper(s, start + 1, end - 1, mem) + 2
        else:
            if mem[start + 1][end]:
                res1 = mem[start + 1][end]
            else:
                res1 = self.helper(s, start + 1, end, mem)
            if mem[start][end - 1]:
                res2 = mem[start][end - 1]
            else:
                res2 = self.helper(s, start, end - 1, mem)
            res = max(res1, res2)
        mem[start][end] = res
        return res
        
        
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        mem = [[0 for _ in xrange(len(s))] for _ in xrange(len(s))]
        return self.helper(s, 0, len(s) - 1, mem)


class Solution_2(object):# O(n^2) time in all settings. TLE for Python but AC for Java, C++
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0 for _ in xrange(n)] for _ in xrange(n)]
        for i in xrange(n):
            dp[i][i] = 1
        
        for l in xrange(2, n + 1):
            for start in xrange(0, n - l + 1):
                end = start + l - 1
                if s[start] != s[end]:
                    dp[start][end] = max(dp[start + 1][end], dp[start][end - 1])
                else:
                    dp[start][end] = dp[start + 1][end - 1] + 2
        return dp[0][n - 1]