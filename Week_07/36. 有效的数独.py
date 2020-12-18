class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        n = len(board)
        rows = [{} for i in range(n)]
        cols = [{} for i in range(n)]
        boxes = [{} for i in range(n)]

        for i in range(n):
            for j in range(n):
                tmp = board[i][j]
                if tmp != '.':
                    number = (i / 3) * 3 + j / 3
                    rows[i][tmp] = rows[i].get(tmp, 0) + 1
                    cols[j][tmp] = cols[j].get(tmp, 0) + 1
                    boxes[number][tmp] = boxes[number].get(tmp, 0) + 1
                    if rows[i][tmp] > 1 or cols[j][tmp] > 1 or boxes[number][tmp] > 1:
                        return False
        return True
