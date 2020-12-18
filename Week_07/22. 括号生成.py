class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        visited, queue = [], [('', 0, 0)]
        while queue:
            tmp, l, r = queue.pop(0)
            if r == n:
                visited.append(tmp)
            if l < n:
                queue.append((tmp + '(', l + 1, r))
            if l > r:
                queue.append((tmp + ')', l, r + 1))
        return visited
