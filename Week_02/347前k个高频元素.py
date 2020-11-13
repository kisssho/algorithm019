import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hash_nums = {}
        for i,j in enumerate(nums):
            hash_nums[j] = hash_nums.get(j,0)+1
        res = heapq.nlargest(k,hash_nums.items(),lambda s:s[1])
        return [i[0] for i in res]