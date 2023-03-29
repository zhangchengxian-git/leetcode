/*
 * @lc app=leetcode.cn id=58 lang=java
 *
 * [58] 最后一个单词的长度
 */

// @lc code=start
class Solution {
    public int lengthOfLastWord(String s) {
        s = s.trim();
        for(int i=s.length()-1; i>-1; i--){
            if (s.charAt(i)==' '){
                return s.length()-i-1;
            }
        }
        return s.length();
    }
}
// @lc code=end

