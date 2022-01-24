class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        N = len(nums)
        if N < 2:
            return 0
        
        sell_price = nums[1]
        buy_price = nums[0]
        max_profit = sell_price - buy_price
        
        for i in range(N):
            
            buy_price = min(buy_price, nums[i])
            potential_profit = nums[i] - buy_price
            max_profit = max(potential_profit, max_profit)
            
            
        if max_profit <= 0 :
            return -1
        
        return max_profit
        