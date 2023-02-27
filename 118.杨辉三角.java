import java.util.ArrayList;
import java.util.List;

/*
 * @lc app=leetcode.cn id=118 lang=java
 *
 * [118] 杨辉三角
 */

// @lc code=start
class Solution {
    public List<List<Integer>> generate(int numRows) {

    }

    public List<Integer> getNum(int row){
        List<Integer> nums = new ArrayList<>();
        nums.add(1); 
        if(row==0){
            return nums;
        }
        for(int i=1; i<row/2+1; i++){
            nums.add(nums.get(i-1)*(row-i+1)/i);
        }
        if(row/2 == 0){
        
        }
    }
}
// @lc code=end

