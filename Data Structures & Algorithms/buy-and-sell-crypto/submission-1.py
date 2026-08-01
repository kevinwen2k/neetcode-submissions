class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float("inf")
        for p in prices:
            min_price = min(min_price, p)
            max_profit = max(p - min_price, max_profit)

        return max_profit
            