class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        dic = {}

        def recursion(i, j):
            if (i, j) in dic:
                return dic[(i, j)]
            if i == n - 1 and j == m - 1:
                return 1
            count = 0
            if i < n - 1:
                count += recursion(i + 1, j)
            if j < m - 1:
                count += recursion(i, j + 1)
            dic[(i, j)] = count
            return dic[(i, j)]

        return recursion(0, 0)
