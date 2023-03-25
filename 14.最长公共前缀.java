/*
 * @lc app=leetcode.cn id=14 lang=java
 *
 * [14] 最长公共前缀
 */

// @lc code=start
class Solution {
    public String longestCommonPrefix(String[] strs) {
        if(strs[0].length() == 0){
            return "";
        }
        if(strs.length==1){
            return strs[0];
        }
        StringBuffer res = new StringBuffer("");
        int column = 0;
        Character ch = strs[0].charAt(column);
        while(true){
            for(int row=1; row<strs.length; row++){
                if(column>=strs[row].length()){
                    return res.toString();
                }else{
                    if(strs[row].charAt(column) == ch && row == strs.length-1){
                        res.append(ch);
                        column ++;
                        if(column < strs[0].length()){
                            ch = strs[0].charAt(column);
                        }else{
                            return res.toString();
                        }
                    }
                    else if(strs[row].charAt(column) != ch){
                        return res.toString();
                    }
                }
            }
        }
    }
}
// @lc code=end

