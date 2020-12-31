class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        def dfs(n, dp):
            if not dp[n]:
                dp[n] = dfs(n - 1, dp) + dfs(n - 2, dp)
            return dp[n]
        return dfs(n, dp)