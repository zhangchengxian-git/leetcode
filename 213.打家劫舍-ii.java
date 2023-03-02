import java.util.Arrays;

/*
 * @lc app=leetcode.cn id=213 lang=java
 *
 * [213] 打家劫舍 II
 */

// @lc code=start
class Solution {
    public int rob(int[] nums) {
        if(nums.length==1){
            return nums[0];
        }
        if(nums.length==2){
            return Math.max(nums[0], nums[1]);
        }
        return Math.max(robNums(Arrays.copyOfRange(nums, 0, nums.length-1)), robNums(Arrays.copyOfRange(nums, 1, nums.length)));
    }
    public int robNums(int[] nums){
        int[] dp = new int[2];
        dp[0] = nums[0];
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

