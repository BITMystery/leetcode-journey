class Solution(object):
    def dfs(self, k, n, start, path, res):
        if n > 0 and len(path) == k:
            return # bad leaf
        if n < 0:
            return # bad leaf
        if n == 0 and len(path) == k:
            res.append(path) # good leaf
            return
        for i in xrange(start, 10):
            if i > n:
                break
            self.dfs(k, n - i, i + 1, path + [i], res)
            
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(k, n, 1, [], res)
        return res
