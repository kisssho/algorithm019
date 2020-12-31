class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        dic = dict()
        for i,c in enumerate(s):
            dic[c] = dic.get(c, 0) + 1
        for i,c in enumerate(s):
            if dic[c] == 1:
                return i
        return -1