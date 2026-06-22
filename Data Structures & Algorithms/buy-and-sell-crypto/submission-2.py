class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        high = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                value = prices[j]-prices[i]
                if value >= high:
                    high = value
        return high

        