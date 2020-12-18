class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        if not m or not grid[0]:
            return 0
        n = len(grid[0])

        def dfs(x, y):
            if x == n or x == -1 or y == -1 or y == m or grid[y][x] != '1':
                return
            grid[y][x] = 'x'
            dfs(x + 1, y)
            dfs(x, y + 1)
            dfs(x - 1, y)
            dfs(x, y - 1)

        count = 0
        for y, i in enumerate(grid):
            for x, j in enumerate(i):
                if j == '1':
                    count += 1
                    dfs(x, y)
        return count

