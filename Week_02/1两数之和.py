class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_nums = {}
        for i,j in enumerate(nums):
            k = hash_nums.get(j)
            if k is not None:
                return [i,k]
            hash_nums[target-j]=i