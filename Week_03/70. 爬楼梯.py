class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [0] * (n + 1)
        return self.climb(0, n, res)

    def climb(self, level, n, res):
        if level > n:
            return 0
        if level == n:
            return 1
        if res[level] > 0:
            return res[level]
        res[level] = self.climb(level + 1, n, res) + self.climb(level + 2, n, res)
        return res[level]