/*
 * @lc app=leetcode.cn id=122 lang=java
 *
 * [122] 买卖股票的最佳时机 II
 */

// @lc code=start
class Solution {
    public int maxProfit(int[] prices) {
        int has = 0-prices[0];
        int not_has = 0;
        for(int i=1; i<prices.length; i++){
            int last_not_has = not_has;
            not_has = Math.max(not_has, has+prices[i]);
            has = Math.max(has, last_not_has-prices[i]);
        }
        return Math.max(has, not_has);
    }
}
// @lc code=end

