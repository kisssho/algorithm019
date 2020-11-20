class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = list()
        def recursion(cur,start):
            if len(cur) == k:
                res.append(cur[:])
                return
            for i in range(start,n+1):
                cur.append(i)
                recursion(cur,i+1)
                cur.pop()
        recursion([],1)
        return res
