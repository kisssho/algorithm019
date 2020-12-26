class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        while n != 0 and n & 1 == 0:
            n >>= 1
        return n == 1

