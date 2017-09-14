class Solution(object):
    def validate(self, coordinates, x_offset, y_offset, board):
        s = set()
        for (x, y) in coordinates:
            x, y = x + x_offset, y + y_offset
            c = board[x][y]
            if c == '.':
                continue
            if c < '1' or c > '9':
                return False
            if c in s:
                return False
            else:
                s.add(c)
        return True
    
    
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if len(board) != 9 or len(board[0]) != 9:
            return False
        # validate rows
        row = [(0, y) for y in xrange(9)]
        if any([not self.validate(row, x_offset, 0, board) for x_offset in xrange(9)]):
            return False
        # validate columns
        column = [(x, 0) for x in xrange(9)]
        if any([not self.validate(column, 0, y_offset, board) for y_offset in xrange(9)]):
            return False
        # validate blocks
        block = [(x, y) for x in xrange(3) for y in xrange(3)]
        if any([not self.validate(block, 3 * x_offset,  3 * y_offset, board) for x_offset in xrange(3) for y_offset in xrange(3)]):
            return False
        return True
        