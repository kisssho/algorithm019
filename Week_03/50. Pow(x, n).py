class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n<0:
            n = -n
            x = 1/x
        return self.recursion(x,n)
    def recursion(self,x,n):
        if n==0:
            return 1.0
        half = self.recursion(x,n/2)
        res = 1.0
        if n%2==0:
            res = half*half
        else:
            res = half*half*x
        return res