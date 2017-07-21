class Solution(object):
    def dfs(self, candidates, target, start, path, res):
        if target < 0:
            return # bad leaf
        if target == 0:
            res.append(path) # reach good leaf
            return
        for i in xrange(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > target:
                break
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
