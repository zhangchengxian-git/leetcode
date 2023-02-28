/*
 * @lc app=leetcode.cn id=119 lang=java
 *
 * [119] 杨辉三角 II
 */

// @lc code=start
import java.util.List;
import java.util.ArrayList;

class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> nums = new ArrayList<>();
        List<Integer> nums_reverse = new ArrayList<>();
        nums.add(1); 
        nums_reverse.add(0, 1);
        if(rowIndex==0){
            return nums;
        }
        for(int i=1; i<rowIndex/2+1; i++){
            int a = (int)((long)nums.get(i-1)*(rowIndex-i+1)/i);
            nums.add(a);
            //System.out.println(a);
            nums_reverse.add(0, a);
        }
        if(rowIndex%2 == 0){
            nums_reverse.remove(0);
            nums.addAll(nums_reverse);
            return nums;
        }
        else{
            nums.addAll(nums_reverse);
            return nums;
        }
    }
}

// @lc code=end

