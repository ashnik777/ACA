class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        total = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    total += 1
                    if i < len(board)-1:
                        if board[i+1][j] == 'X':
                            total -= 1
                    if j < len(board[0])-1:
                        if board[i][j+1] == 'X':
                            total -= 1
        return total
