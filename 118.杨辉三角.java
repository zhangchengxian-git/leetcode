import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.List;

/*
 * @lc app=leetcode.cn id=118 lang=java
 *
 * [118] 杨辉三角
 */

// @lc code=start
class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> res = new ArrayList<>();
        for(int i=0; i<numRows; i++){
            List<Integer> row = new ArrayList<>();
            row = getNum(i);
            res.add(row);
        }
        return res;
    }

    public List<Integer> getNum(int row){
        List<Integer> nums = new ArrayList<>();
        List<Integer> nums_reverse = new ArrayList<>();
        nums.add(1); 
        nums_reverse.add(0, 1);
        if(row==0){
            return nums;
        }
        for(int i=1; i<row/2+1; i++){
            int a = nums.get(i-1)*(row-i+1)/i;
            nums.add(a);
            nums_reverse.add(0, a);
        }
        if(row%2 == 0){
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

