class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash_strs = {}
        for i in strs:
            tmp = ''.join(sorted(i))
            hash_strs[tmp] = hash_strs.get(tmp,[])+[i]
        return hash_strs.values()