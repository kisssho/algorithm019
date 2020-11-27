class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res, queue = [], [('', 0, 0)]

        while queue:
            tmp, left, right = queue.pop(0)
            if len(tmp) == 2 * n:
                res.append(tmp)
            if left < n:
                queue.append((tmp + '(', left + 1, right))
            if right < left:
                queue.append((tmp + ')', left, right + 1))
        return res
