dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
END_OF_WORD = "#"


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not words or not board or not board[0]: return []
        self.dx = [1, -1, 0, 0]
        self.dy = [0, 0, 1, -1]

        root = {}
        for w in words:
            cur = root
            for i in w:
                if i not in cur:
                    cur[i] = {}
                cur = cur[i]
            cur['#'] = True
        print(root)
        self.result = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in root:
                    self.dfs(board, '', i, j, root)

        return list(self.result)