class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        count = 0
        gl = len(g)
        sl = len(s)
        for i in range(sl):
            if s[i] >= g[count]:
                count += 1
            if count == gl:
                break
        return count