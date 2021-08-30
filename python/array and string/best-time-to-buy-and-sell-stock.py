#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr = ans = 0
        for i in range(1, len(prices)):
            t = prices[i] - prices[i-1]
            curr = max(t, t+ curr)
            ans = max(ans, curr)
        return ans
