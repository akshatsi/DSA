class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mini = prices[0]
        profit = 0
        for i in prices:
            if i < mini:
                mini = i
            else:
                profit = max(profit, i-mini)
        return profit




