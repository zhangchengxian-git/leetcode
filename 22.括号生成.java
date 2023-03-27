import java.util.ArrayList;
import java.util.List;

/*
 * @lc app=leetcode.cn id=22 lang=java
 *
 * [22] 括号生成
 */

// @lc code=start
class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<>();
        StringBuffer tmp = new StringBuffer();
        generate(1, 0, res, tmp.append('('), n);
        return res;
        
    }
    public void generate(int left, int right, List<String> res, StringBuffer tmp, int n) {
        if(left==right && left == n){
            res.add(tmp.toString());
            return;
        }
        if(left < n){
            generate(left+1, right, res, tmp.append('('), n);
            tmp.deleteCharAt(tmp.length()-1);
        }
        if(left>right){
            generate(left, right+1, res, tmp.append(')'), n);
            tmp.deleteCharAt(tmp.length()-1);
        }
    }
}
// @lc code=end

