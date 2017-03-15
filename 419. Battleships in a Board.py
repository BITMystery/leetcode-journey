class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        # Idea: If a point is the head or tail of a ship, only one of its 4 adjacent points is 'X'. Exception: The ship contains only one 'X'.
        #       If a point is an inner node of a ship, two of its 4 adjacent points are 'X's.
        r = 0
        length = len(board)
        width = len(board[0])
        for i in range(0, length):
        	for j in range(0, width):
        		if board[i][j] == 'X':
        			counter = 0
        			# up
        			if i > 0 and board[i - 1][j] == 'X':
        				counter += 1
        			#down
        			if i < length - 1 and board[i + 1][j] == 'X':
        				counter += 1
        			#left
        			if j > 0 and board[i][j - 1] == 'X':
        				counter += 1
        			#right
        			if j < width -1 and board[i][j + 1] == 'X':
        				counter += 1
        			if counter == 0:
        				r += 2
        			elif counter == 1:
        				r += 1
        return r / 2

class Solution_2(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        #Idea: Scan the board, once the left and top neighbor of a point are '.'s, this point counts a ship.
        r = 0
        length = len(board)
        width = len(board[0])
        for i in range(0, length):
        	for j in range(0, width):
        		# Better than solution 1. Only need to judge left and top
        		if board[i][j] == 'X' and (i == 0 or board[i-1][j] == '.') and (j == 0 or board[i][j-1] == '.'):
        			r += 1
        return r

s = Solution()
print s.countBattleships(['X..X', '...X', '...X'])
