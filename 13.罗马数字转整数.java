
import java.util.*;

/*
 * @lc app=leetcode.cn id=13 lang=java
 *
 * [13] 罗马数字转整数
 */

// @lc code=start
class Solution {
    public int romanToInt(String s) {
        Map<Character, Integer> roma = new HashMap<>();
        roma.put('I', 1);
        roma.put('V', 5);
        roma.put('X', 10);
        roma.put('L', 50);
        roma.put('C', 100);
        roma.put('D', 500);
        roma.put('M', 1000);
        int res = 0;
        for(int i=0; i<s.length(); i++){
            if(i == s.length()-1){
                res = res + roma.get(s.charAt(i));
            }else{
                if(roma.get(s.charAt(i))<roma.get(s.charAt(i+1))){
                    res = res - roma.get(s.charAt(i));
                }
                else{
                    res = res + roma.get(s.charAt(i));
                }
            }
        }
        return res;
    }
}
// @lc code=end

