class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        def solve(board):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == '.':
                        for k in '123456789':
                            if valid(board, i, j, k):
                                board[i][j] = k
                                if solve(board):
                                    return True
                                else:
                                    board[i][j] = '.'
                        return False
            return True

        def valid(board, row, col, num):
            for i in range(len(board)):
                if board[i][col] == num:
                    return False
                if board[row][i] == num:
                    return False
                if board[3 * (row / 3) + i / 3][3 * (col / 3) + i % 3] == num:
                    return False
            return True

        return solve(board)