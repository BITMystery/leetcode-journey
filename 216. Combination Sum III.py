class Solution(object):
    def dfs(self, start, k, target, path, res):
        if target < 0:
            return # bad leaf
        if target > 0:
            if len(path) >= k:
                return # bad leaf
        if target == 0:
            if len(path) == k:
                res.append(path)
            return
        for i in xrange(start, 10):
            self.dfs(i + 1, k, target - i, path + [i], res)
            
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(1, k, n, [], res)
        return res
