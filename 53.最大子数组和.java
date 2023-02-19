/*
 * @lc app=leetcode.cn id=53 lang=java
 *
 * [53] 最大子数组和
 */

// @lc code=start
class Solution {
    public int maxSubArray(int[] nums) {
        int dp = nums[0];
        int maxSub = dp;
        for(int i=1; i < nums.length; i++){
            if (dp > 0){
                dp = dp + nums[i];
            }
            else{
                dp = nums[i];
            }
            if (dp > maxSub){
                maxSub = dp;
            }
        }
        return maxSub;
    }
}
// @lc code=end

