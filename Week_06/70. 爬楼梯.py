class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        f1, f2 = 1, 1
        for i in range(2, n + 1):
            f1, f2 = f2, f1 + f2
        return f2