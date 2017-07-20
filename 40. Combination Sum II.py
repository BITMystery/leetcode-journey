class Solution(object):
    def dfs(self, candidates, target, start, path, res):
        if target == 0:
            res.append(path) # good leaf
            return
        if target < 0:
            return # bad leaf
        for i in xrange(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            self.dfs(candidates, target - candidates[i], i + 1, path + [candidates[i]], res)
            
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res