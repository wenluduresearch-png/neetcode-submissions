class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        low_idx, high_idx = 0, 0
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < prices[low_idx]:
                low_idx = high_idx = i
            if prices[i] > prices[high_idx]:
                high_idx = i
                max_profit = max(max_profit, prices[high_idx] - prices[low_idx]) 
        return max_profit
