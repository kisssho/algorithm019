class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.res = []
        self.dfs(0, 0, 0, 0, [], n)
        return [['.' * j + 'Q' + '.' * (n - j - 1) for j in i] for i in self.res]

    def dfs(self, level, col, pie, na, queens, n):
        if level == n:
            self.res.append(queens)
            return
        bits = (~(col | pie | na) & ((1 << n) - 1))
        while bits:
            p = bits & - bits
            bits &= (bits - 1)
            site =  bin(p - 1)[2:].count('1')
            self.dfs(level + 1, col | p, (pie | p) << 1, (na | p) >> 1, queens + [site], n)