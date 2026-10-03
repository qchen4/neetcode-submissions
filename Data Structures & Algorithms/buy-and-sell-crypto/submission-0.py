class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        lowest = prices[0]
        for i in range(len(prices)):
            maxProfit = max(maxProfit, prices[i] - lowest)
            lowest = min(lowest, prices[i])
        return maxProfit



        