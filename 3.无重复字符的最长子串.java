import java.util.HashSet;
import java.util.Set;

/*
 * @lc app=leetcode.cn id=3 lang=java
 *
 * [3] 无重复字符的最长子串
 */

// @lc code=start
class Solution {
    public int lengthOfLongestSubstring(String s) {
        if(s.length()==0){
            return 0;
        }
        int left, right, max_length, length;
        left = right = max_length = length = 0;
        Set<Character> charSet = new HashSet<>();
        while(left<s.length()-max_length && right<s.length()){
            if(!charSet.contains(s.charAt(right))){
                charSet.add(s.charAt(right));
                length += 1;
                right += 1;
            }else{
                if(max_length<length){
                    max_length = length;
                }
                length -= 1;
                charSet.remove(s.charAt(left));
                left += 1;
            }
        }
        if(max_length<length){
            max_length = length;
        }
        return max_length;
    }
}
// @lc code=end

