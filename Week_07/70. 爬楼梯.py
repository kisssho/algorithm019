class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]*(n + 1)
        dp[0], dp[1] = 1, 1
        def recursion(level):
            if level < 0:
                return
            if dp[level]:
                return dp[level]
            dp[level] = recursion(level - 1) + recursion(level - 2)
            return dp[level]
        return recursion(n)