/*
 * @lc app=leetcode.cn id=121 lang=java
 *
 * [121] 买卖股票的最佳时机
 */

// @lc code=start
class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;
        int minPrice = prices[0];
        for(int i=1; i<prices.length; i++){
            minPrice = Math.min(prices[i], minPrice);
            profit = Math.max(profit, prices[i]-minPrice);
        }
        return profit;
    }
}
// @lc code=end

