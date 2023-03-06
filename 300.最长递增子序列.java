import java.util.ArrayList;
import java.util.List;
/*
 * @lc app=leetcode.cn id=300 lang=java
 *
 * [300] 最长递增子序列
 */


// @lc code=start
class Solution {
    public int lengthOfLIS(int[] nums) {
        List<Integer> dp = new ArrayList<Integer>();
        dp.add(nums[0]);
        int length = 1;
        for(int i=1; i<nums.length; i++){
            if(nums[i] > dp.get(length-1)){
                length += 1;
                dp.add(nums[i]);
            }else{
                if(dp.contains(nums[i])){
                    continue;
                } 
                else{
                    dp.set(getFirstBig(dp, nums[i], 0, length-1), nums[i]);
                    
                }
            }
        }
        return length;
    }

    private int getFirstBig(List<Integer> nums, int num, int begin, int end){
        int pos = end;
        while(begin<end){
            int mid = (begin+end)/2;
            if(nums.get(mid)>num){
                end = mid;
                pos = end;
            }else{
                begin = mid+1;
            }
        }
        return pos;
    }
}
// @lc code=end

