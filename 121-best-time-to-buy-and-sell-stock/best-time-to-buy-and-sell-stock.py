class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mini = prices[0]
        profit = 0
        for i in prices:
            mini = min(i,mini)

            a = i-mini
            profit = max(profit,a)
        return profit




