#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            minPrice = min(minPrice, prices[i])
            profit = max(profit, prices[i]-minPrice)
        return profit
# @lc code=end

