class Solution(object):
    def backtracking(self, digits, index, level, path, res):
        if level == len(digits):
            if path != '':
                res.append(path) # leaf
            return
        for c in index[int(digits[level]) - 1]:
            self.backtracking(digits, index, level + 1, path + c, res)
            
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        index = ['', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        res = []
        self.backtracking(digits, index, 0, '', res)
        return res