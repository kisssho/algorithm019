class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        array_s,array_t = [0]*26,[0]*26
        for i in s:
            array_s[ord(i)-ord('a')] +=1
        for i in t:
            array_t[ord(i)-ord('a')] +=1
        return array_s==array_t