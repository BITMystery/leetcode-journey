class Solution(object):
    def get_state(self, board, i, j):
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
            return 0
        return board[i][j]
    
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # first-pass: 0 -> 0: 0, 1 -> 1: 1, 0 -> 1: 2, 1 -> 0: 3
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                before = board[i][j]
                lives = 0 # number of live neighbors
                for k in xrange(-1, 2):
                    for l in xrange(-1, 2):
                        lives += self.get_state(board, i + k, j + l) % 2
                lives -= before
                if before == 0 and lives == 3:
                    board[i][j] = 2
                elif before == 1 and (lives < 2 or lives > 3):
                    board[i][j] = 3
        # second-pass: 0 -> 0, 1 -> 1, 2 -> 1, 3 -> 0
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == 3:
                    board[i][j] = 0
        