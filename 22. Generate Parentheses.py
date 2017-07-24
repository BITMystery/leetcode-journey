class Solution(object):
    def backtrack(self, left, right, path, res):
        if left > right or left < 0 or right < 0:
            return # illegal combination
        if left == 0 and right == 0:
            res.append(path) # legal combination
            return
        self.backtrack(left - 1, right, path + '(', res)
        self.backtrack(left, right - 1, path + ')', res)
        
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.backtrack(n, n, '', res)
        return res