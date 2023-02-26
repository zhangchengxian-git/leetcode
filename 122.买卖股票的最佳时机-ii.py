#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        has, not_has = 0-prices[0], 0
        for i in range(1, len(prices)):
            last_not_has = not_has
            not_has = max(not_has, has+prices[i])
            has = max(has, last_not_has-prices[i])
        return max(has, not_has)
# @lc code=end

