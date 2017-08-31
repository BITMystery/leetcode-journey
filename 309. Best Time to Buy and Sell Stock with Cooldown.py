class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) == 1:
            return 0
        # day 0
        buy, sell, sell_yesterday = -prices[0], 0, 0
        
        # loop from day 1
        for day in xrange(1, len(prices)):
            buy_today = max(buy, sell_yesterday - prices[day])
            sell_today = max(sell, buy + prices[day])
            sell_yesterday = sell
            buy, sell = buy_today, sell_today
        return sell