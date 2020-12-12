class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = float('-inf')
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                tmp = sum(nums[i:j+1])
                if tmp > res:
                    res = tmp
        return res