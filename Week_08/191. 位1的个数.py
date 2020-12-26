class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n:
            return self.hammingWeight(n & (n - 1)) + 1
        return 0