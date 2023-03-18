/*
 * @lc app=leetcode.cn id=8 lang=java
 *
 * [8] 字符串转换整数 (atoi)
 */

// @lc code=start
class Solution {
    public int myAtoi(String s) {
        s = s.strip();
        Boolean plus = true;
        Boolean add_plus = false;
        long res = 0;
        long MAX = (long)Math.pow(2, 31)-1;
        Long MIN = -(long)(Math.pow(2, 31));
        for(int i=0; i<s.length(); i++){
            if(!add_plus && s.charAt(i)=='-'){
                plus = false;
                add_plus = true;
            }else if (!add_plus && s.charAt(i)=='+'){
                add_plus = true;
            }else if (Character.isDigit(s.charAt(i))){
                if(plus){
                    if(res*10+((int)(s.charAt(i))-(int)('0'))>MAX){
                        return (int)MAX;
                    }else{
                        res = res*10+((int)(s.charAt(i))-(int)('0'));
                    }
                }else{
                    if(res*10-((int)(s.charAt(i))-(int)('0'))<MIN){
                        return (int)(-Math.pow(2, 31));
                    }else{
                        res = res*10-((int)(s.charAt(i))-(int)('0'));
                    }
                }
                add_plus = true;
            }else if (!Character.isDigit(s.charAt(i))){
                break;
            }
        }
        return (int)res;
    }
}
// @lc code=end

