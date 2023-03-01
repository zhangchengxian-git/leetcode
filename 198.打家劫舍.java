/*
 * @lc app=leetcode.cn id=198 lang=java
 *
 * [198] 打家劫舍
 */

// @lc code=start
class Solution {
    public int rob(int[] nums) {
        int[] dp = new int[2];
        dp[0] = nums[0];
        if(nums.length==1){
            return dp[0];
        }
        dp[1] = Math.max(nums[0], nums[1]);
        for(int i=2; i<nums.length; i++){
            int tmp = Math.max(dp[0]+nums[i], dp[1]);
            dp[0] = dp[1];
            dp[1] = tmp;
        }
        return Math.max(dp[0], dp[1]);
    }
}
// @lc code=end

