class Solution(object):
    def adjacentSquares(self, board, row, col):
    	#Sequence: lt, t, rt, r, rb, b, lb, l
    	l = [[row-1, col-1], [row-1, col], [row-1, col+1], [row, col+1], [row+1, col+1], [row+1, col], [row+1, col-1], [row, col-1]]
    	adj = []
    	for [r, c] in l:
    		if 0 <= r < len(board) and 0 <= c < len(board[0]):
    			if board[r][c] == 'M' or board[r][c] == 'E':
    				adj.append([r, c])
    	return adj

    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        row = click[0]
        col = click[1]
        #Case 1: A mine ('M') is revealed
        if board[row][col] == 'M':
        	board[row][col] = 'X'
        	return board
        adj = self.adjacentSquares(board, row, col)
        num_adj_mines = 0
        for [r, c] in adj:
        	if board[r][c] == 'M':
        		num_adj_mines += 1
        #Case 2: An empty square ('E') with at least one adjacent mine is revealed
        if num_adj_mines > 0:
        	board[row][col] = str(num_adj_mines)
        #Case 3: An empty square ('E') with no adjacent mines is revealed
    	else:
    		board[row][col] = 'B'
    		for s in adj:
    			self.updateBoard(board, s)
    	return board

s = Solution()
print s.updateBoard(['B1E1B', 'B1M1B', 'B111B', 'BBBBB'], [1,2])