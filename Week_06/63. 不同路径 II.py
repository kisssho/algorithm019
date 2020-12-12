class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        self.grid = obstacleGrid
        self.h = len(self.grid) - 1
        self.w = len(self.grid[0]) - 1
        self.count = 0
        self.d = dict()
        if self.grid[0][0] != 1:
            return self.dfs(0, 0)
        return 0

    def dfs(self, i, j):
        if (i, j) in self.d:
            return self.d[(i, j)]

        if i == self.h and j == self.w:
            return 1
        s = 0
        for x, y in [(i, j + 1), (i + 1, j)]:
            if x >= 0 and y >= 0 and x < len(self.grid) and y < len(self.grid[0]) and self.grid[x][y] == 0:
                s += self.dfs(x, y)

        self.d[(i, j)] = s

        return self.d[(i, j)]
