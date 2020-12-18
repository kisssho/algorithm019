class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []

        def recursion(level, tmp, t1, t2):
            if level == n:
                if len(tmp) == n:
                    res.append(tmp)
                return
            for i in range(n):
                if i in tmp or i + level in t1 or level - i in t2:
                    continue
                recursion(level + 1, tmp + [i], t1 + [level + i], t2 + [level - i])

        recursion(0, [], [], [])
        return [['.' * j + 'Q' + '.' * (n - 1 - j) for j in i] for i in res]
