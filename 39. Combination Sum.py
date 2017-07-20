class Solution(object):
    def dfs(self, candidates, target, start, path, res):
        if target == 0:
            res.append(path) #good leaf
            return
        if target < 0:
            return #bad leaf
        for i in xrange(start, len(candidates)):
            self.dfs(candidates, target - candidates[i], i, path + [candidates[i]], res)
        
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        start = 0
        cur_path = []
        res = []
        self.dfs(candidates, target, start, cur_path, res)
        return res

s = Solution()
print s.combinationSum([2, 3, 4, 7], 7)