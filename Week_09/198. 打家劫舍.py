class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f1, f2 = 0, 0
        for i in range(len(nums)):
            f1, f2 = f2, max(f1 + nums[i], f2)
        return f2