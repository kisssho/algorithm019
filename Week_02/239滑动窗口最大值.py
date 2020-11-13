import heapq
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # if k<=1:
        #     return nums
        res,heap,i = [],[],0
        while i<len(nums):
            start = i-k
            if start>=0:
                while len(heap)>=1 and heap[0][1]<=start:
                    heapq.heappop(heap)
            heapq.heappush(heap,(-nums[i],i))
            if len(heap)>=k:
                res.append(-heap[0][0])
            i+=1
        return res