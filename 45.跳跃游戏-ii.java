/*
 * @lc app=leetcode.cn id=45 lang=java
 *
 * [45] 跳跃游戏 II
 */

// @lc code=start
class Solution {
    public int jump(int[] nums) {
        int n = nums.length;
        int maxPos = 0;
        int end = 0;
        int step = 0;
        for(int i=0; i<n-1; i++){
            if (maxPos >= i){
                maxPos = Math.max(maxPos, i + nums[i]);
            }
            if (i == end){
                end = maxPos;
                step += 1;
            }
                
        }
        return step;
    }
}
// @lc code=end

