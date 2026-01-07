class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minimum_price = prices[0]
        profit = 0
        for current_price in prices:
            if current_price < minimum_price:
                minimum_price = current_price
            else:
                profit = max(profit, current_price-minimum_price)
        return profit




