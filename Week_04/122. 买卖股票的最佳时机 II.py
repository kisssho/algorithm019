class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                count += prices[i + 1] - prices[i]
        return count