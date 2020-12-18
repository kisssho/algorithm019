class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        m = len(M)
        p = [i for i in range(m)]

        def find(p, i):
            root = i
            while p[root] != root:
                root = p[root]
            while p[i] != i:
                x = i;
                i = p[i];
                p[x] = root
            return root

        def union(p, i, j):
            rootA = find(p, i)
            rootB = find(p, j)
            p[rootA] = rootB

        for i in range(m):
            for j in range(m):
                if M[i][j] == 1:
                    union(p, i, j)
        res = 0
        for i in range(m):
            if p[i] == i:
                res += 1
        return res