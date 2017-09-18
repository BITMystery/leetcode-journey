class Solution(object):
    def is_valid(self, board, i, j):
        for k in xrange(9):
            if k != j and board[i][k] == board[i][j]:
                return False
            if k != i and board[k][j] == board[i][j]:
                return False
        for s in xrange(i / 3 * 3, i / 3 * 3 + 3):
            for t in xrange(j / 3 * 3, j / 3 * 3 + 3):
                if (s, t) != (i, j) and board[s][t] == board[i][j]:
                    return False
        return True
    
    
    def solve(self, board):
        for i in xrange(9):
            for j in xrange(9):
                if board[i][j] == '.':
                    for k in xrange(1, 10):
                        board[i][j] = str(k)
                        if self.is_valid(board, i, j) and self.solve(board):
                            return True
                        board[i][j] = '.'
                    return False
        return True
    
    
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        for i in xrange(9):
            board[i] = list(board[i])
        self.solve(board)
        for i in xrange(9):
            board[i] = ''.join(board[i])