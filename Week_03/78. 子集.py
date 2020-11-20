class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = [[]]

        for i in range(len(nums)):
            tmp = []
            for j in range(len(res)):
                tmp.append(res[j]+[nums[i]])
            res.extend(tmp)
        return res