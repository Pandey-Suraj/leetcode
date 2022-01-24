class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        N = len(prices)
        if N <2:
            return 0
        buy = prices[0]
        sell = prices[1]
        max_profit = sell - buy
        
        for i in range(len(prices)):
            buy = min(buy,prices[i])
            margin = prices[i] - buy 
            max_profit = max(max_profit,margin)
            
        return max_profit