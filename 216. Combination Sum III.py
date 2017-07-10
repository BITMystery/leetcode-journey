class Solution(object):
    def Combinations(self, k, n, min_num):
        if k < 0 or k > 9  or n < (2 * min_num + k - 1) * k / 2 or n > (19 - k) * k / 2:
            return []
        if k == 1:
            return [[n]]
        res = []
        for i in xrange(min_num + 1, 10):
            tmp = self.Combinations(k - 1, n - i + 1, i)
            for comb in tmp:
                res.append([i - 1] + comb)
        return res
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        return self.Combinations(k, n, 1)

s = Solution()
print s.combinationSum3(3, 7)
        