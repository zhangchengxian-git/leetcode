import java.util.ArrayList;
import java.util.List;

/*
 * @lc app=leetcode.cn id=6 lang=java
 *
 * [6] N 字形变换
 */

// @lc code=start
class Solution {
    public String convert(String s, int numRows) {
        if(s.length()==1 || numRows==1 || numRows>=s.length()){
            return s;
        }
        String res = "";
        int left = 2*numRows-2;
        int right = 0;
        int j = 0;
        for(int i=0; i<numRows; i++){
            j = i;
            if(left==2*numRows-2){
                while(j<s.length()){
                    res = res.concat(String.valueOf(s.charAt(j)));
                    j = j+left;
                }
                left = left-2;
                right = 2*numRows-2-left;
            }else if(right == 2*numRows-2){
                
                while(j<s.length()){
                    res = res.concat(String.valueOf(s.charAt(j)));
                    j = j+right;
                }
            }
            else{
                Boolean up = true;
                while(j<s.length()){
                    res = res.concat(String.valueOf(s.charAt(j)));
                    if(up){
                        up = false;
                        j = j+left;
                    }else{
                        up = true;
                        j=j+right;
                    }
                }
                left = left-2;
                right = right+2;

            }
        }
        return res;
    }
}
// @lc code=end

