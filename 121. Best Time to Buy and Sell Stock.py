class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if None == prices or len(prices) == 0:
            return 0
        max_profit = 0
        low = high = prices[0]
        for i in xrange(1, len(prices)):
            if prices[i] < low:
                low = high = prices[i]
            elif prices[i] > high:
                high = prices[i]
                profit = high - low
                if profit > max_profit:
                    max_profit = profit
        return max_profit