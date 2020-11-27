class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        end = len(nums) - 1
        for i in range(len(nums))[::-1]:
            if nums[i] + i >= end:
                end = i
        return end == 0
