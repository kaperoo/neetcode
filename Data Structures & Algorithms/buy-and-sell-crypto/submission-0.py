class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        for i in range(1,len(prices)):
            for j in range(len(prices)-i):
                profit = prices[j+i] - prices[j]
                if profit > max_profit:
                    max_profit = profit

        return max_profit