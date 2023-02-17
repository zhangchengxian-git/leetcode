/*
 * @lc app=leetcode.cn id=55 lang=java
 *
 * [55] 跳跃游戏
 */

// @lc code=start
class Solution {
    public boolean canJump(int[] nums) {
        int far = 0;
        for(int i=0; i<nums.length; i++){
            if (i > far){
                return false;
            }
            far = Math.max(far, nums[i]+i);
        }
        return true;
    }
}
// @lc code=end

